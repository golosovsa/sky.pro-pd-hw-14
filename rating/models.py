"""
    rating blueprint
    models
"""

# global inputs
from dataclasses import dataclass

# local imports
from app_data import AppData
from grm import do_sqlite_dict_factory, BaseModel


class Rating(BaseModel):
    """ Movies by rating model """
    def __init__(self, ratings, limit, offset):

        def is_rating(rating):
            return rating in ratings

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory
            conn.create_function("IS_RATING", 1, is_rating)

            cursor = conn.execute("""
                SELECT `title`, `rating`, `description` FROM netflix
                WHERE IS_RATING(`rating`)
                AND `title` IS NOT NULL 
                AND `title` != ""
                AND `description` IS NOT NULL 
                AND `description` != ""
                ORDER BY release_year DESC
                LIMIT :limit
                OFFSET :offset
            """, locals())

            self._data = cursor.fetchall()

