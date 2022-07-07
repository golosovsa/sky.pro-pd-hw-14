"""
    genre blueprint
    models
"""


from app_data import AppData
from grm import do_sqlite_dict_factory, BaseModel


class Together(BaseModel):

    def __init__(self, actor1, actor2, times, limit, offset):

        filter_actor_1 = f"%{actor1}%"
        filter_actor_2 = f"%{actor2}%"

        with AppData() as conn:
            conn.row_factory = do_sqlite_dict_factory

            cursor = conn.execute("""
                WITH RECURSIVE split(item, other) AS (
                    SELECT NULL, TRIM(`cast`)||","
                    FROM netflix
                    WHERE `cast` LIKE :filter_actor_1
                    AND `cast` LIKE :filter_actor_2
                    UNION ALL
                    SELECT
                        TRIM(SUBSTR(other, 0, INSTR(other, ","))),
                        SUBSTR(other, INSTR(other, ",")+1)
                    FROM split WHERE other!=""
                )
                SELECT item AS actor, COUNT(*) AS total FROM split
                WHERE actor NOT IN (:actor1, :actor2)
                GROUP BY actor
                HAVING total > :times
                LIMIT :limit
                OFFSET :offset
            """, locals())

            self._data = cursor.fetchall()
