"""
    genre blueprint
    views
"""


# local imports
from app_data import AppData
from grm import do_sqlite_dict_factory, BaseModel


class GenreTop(BaseModel):
    """ Top 10 genre model """
    def __init__(self, genre):
        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory

            cursor = conn.execute("""
                       SELECT `title`, `description` FROM netflix
                       WHERE `listed_in` LIKE :genre
                       AND `title` IS NOT NULL 
                       AND `title` != ""
                       AND `description` IS NOT NULL 
                       AND `description` != ""
                       ORDER BY release_year DESC
                       LIMIT 10
                   """, {"genre": f"%{genre}%"})

            self._data = cursor.fetchall()
