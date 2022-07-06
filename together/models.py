"""
    genre blueprint
    models
"""


from app_data import AppData
from grm import do_sqlite_dict_factory, BaseModel


class Together(BaseModel):

    def __init__(self, actor, times, limit, offset):

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory
            conn.re

            cursor = conn.execute("""
                WITH RECURSIVE split(value, str) AS (
                    
                )
            """, locals())

            self._data = cursor.fetchall()
