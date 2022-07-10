"""
    blueprint search
    models
"""


# local imports
from grm import do_sqlite_dict_factory, BaseModel
from app_data import AppData


class Search(BaseModel):
    """ Search movies by type, year, genre model """
    def __init__(self, movie_type, release_year, genre, limit, offset):

        genre = f"%{genre}%"

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory

            cursor = conn.execute("""
                SELECT `title`, `description` 
                FROM netflix
                WHERE `type` = :movie_type
                AND `release_year` = :release_year
                AND `listed_in` LIKE :genre
                LIMIT :limit
                OFFSET :offset
            """, locals())

            self._data = cursor.fetchall()
