"""
    movie blueprint
    models
"""


# global imports
from dataclasses import dataclass, field, fields


# local imports
from app_data import AppData
import grm


@dataclass(frozen=True)
class Single:
    title: str
    country: str
    release_year: int
    genre: str = field(metadata={"column": "listed_in"})
    description: str


class SingleModel:

    def __init__(self, title):

        self._result = None

        # get column names from dataclass, it's safe
        json_headers = grm.get_fields_str_for_sqlite_json_function(Single)

        query = (
            f"""
                SELECT json_object({json_headers}) 
                FROM `netflix`
                WHERE netflix.title LIKE :title
                ORDER BY netflix.release_year DESC
                LIMIT 1
            """, {"title": f"%{title}%"}
        )

        with AppData() as connection:
            cursor = connection.cursor()

            cursor.execute(*query)
            self._result = cursor.fetchall()[0][0]

    @property
    def result(self):
        return self._result


@dataclass
class Short:
    title: str
    release_year: int


class ShortModel:

    def __init__(self, start, end, limit, offset):
        self._result = None

        # get column names from dataclass, it's safe
        json_headers = grm.get_fields_str_for_sqlite_json_function(Short)
        column_headers = grm.get_fields_str_from_dataclass(Short)

        query = (
            f"""
            SELECT json_group_array(json_object({json_headers})) FROM (
                SELECT {column_headers} FROM netflix
                WHERE `release_year` BETWEEN :start AND :end
                AND netflix.title IS NOT NULL
                AND netflix.title != ""
                ORDER BY netflix.release_year DESC
                LIMIT :limit
                OFFSET :offset
            )
            """, dict(start=start, end=end, limit=limit, offset=offset)
        )

        with AppData() as connection:
            cursor = connection.cursor()

            cursor.execute(*query)
            self._result = cursor.fetchall()[0][0]

        print(self._result)

    @property
    def result(self):
        return self._result
