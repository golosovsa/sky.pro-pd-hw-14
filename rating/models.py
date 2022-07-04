"""
    rating blueprint
    models
"""

# global inputs
from dataclasses import dataclass

# local imports
from app_data import AppData
import grm


@dataclass
class Rating:
    title: str
    rating: str
    description: str


class RatingModel:

    def __init__(self, rating, limit, offset):
        self._result = None

        # get column names from dataclass, it's safe
        json_headers = grm.get_fields_str_for_sqlite_json_function(Rating)
        column_headers = grm.get_fields_str_from_dataclass(Rating)

        query = (
            f"""
                    SELECT json_group_array(json_object({json_headers})) FROM (
                        SELECT {column_headers} FROM netflix
                        WHERE `rating` IN ({[", ".join("?" * len(rating))]})
                        AND netflix.title IS NOT NULL
                        AND netflix.title != ""
                        AND netflix.description IS NOT NULL 
                        AND netflix.description != ""
                        ORDER BY netflix.title
                        LIMIT :limit
                        OFFSET :offset
                    )
                    """, rating, *dict(rating=rating, limit=limit, offset=offset)
        )

        with AppData() as connection:
            cursor = connection.cursor()

            cursor.execute(*query)
            self._result = cursor.fetchall()[0][0]

        print(self._result)

    @property
    def result(self):
        return self._result
