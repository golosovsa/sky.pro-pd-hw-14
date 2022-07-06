"""
    movie blueprint
    models
"""


# global imports
import sqlite3
from flask import jsonify

# local imports
from app_data import AppData
from grm import do_sqlite_dict_factory, BaseModel


class Single(BaseModel):

    def __init__(self, title):

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory

            cursor = conn.execute("""
                SELECT `title`, `country`, `release_year`, `listed_in` AS `genre`, `description` 
                FROM netflix
                WHERE `title` LIKE :title
                GROUP BY `release_year`
                LIMIT 1
            """, {"title": f"%{title}%"})

            data = cursor.fetchall()

        self._data = data[0] if len(data) else None


class Short(BaseModel):

    def __init__(self, start, end, limit, offset):

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory

            cursor = conn.execute("""
                SELECT `title`, `release_year` FROM netflix
                WHERE `release_year` BETWEEN :start AND :end
                AND `title` IS NOT NULL 
                AND `title` != ""
                ORDER BY release_year DESC
                LIMIT :limit
                OFFSET :offset
            """, locals())

            self._data = cursor.fetchall()
