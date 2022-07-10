"""
    animals blueprint
    models
"""


# global imports
from werkzeug.exceptions import NotFound


# local inputs
from grm import BaseModel, do_sqlite_dict_factory
from app_data import AppDataHW15


class Animal(BaseModel):
    """ Animal model """

    def __init__(self, pk):

        with AppDataHW15() as conn:
            conn.row_factory = do_sqlite_dict_factory

            # 1 query - kind, name, birthday

            cursor = conn.execute("""
                SELECT kinds.name AS `kind`, animals.name, animals.birthday
                FROM animals
                LEFT JOIN kinds ON animals.kind_id = kinds.id
                WHERE animals.id = :pk
                LIMIT 1
            """, locals())

            animal = cursor.fetchall()

            if len(animal) == 0:
                raise NotFound()

            # 2 query - breeds

            cursor = conn.execute("""
                SELECT breeds.name
                FROM animal_breeds
                LEFT JOIN breeds ON animal_breeds.breed_id = breeds.id
                WHERE animal_breeds.animal_id = :pk
            """, locals())

            breeds = cursor.fetchall()

            # 3 query - colors

            cursor = conn.execute("""
                SELECT colors.name
                FROM animal_colors
                LEFT JOIN colors ON animal_colors.color_id = colors.id
                WHERE animal_colors.animal_id = :pk
            """, locals())

            colors = cursor.fetchall()

            # 4 query - outcomes

            cursor = conn.execute("""
                SELECT 
                    "stray-services".name AS `services`, 
                    statuses.name AS `status`, 
                    outcomes.year,
                    outcomes.month
                FROM outcomes
                LEFT JOIN "stray-services" ON outcomes.service_id = "stray-services".id
                LEFT JOIN statuses ON outcomes.status_id = statuses.id
                WHERE outcomes.animal_id = :pk
                ORDER BY outcomes.year, outcomes.month DESC
            """, locals())

            outcomes = cursor.fetchall()

            self._data = {
                "animal": animal[0],
                "breeds": breeds,
                "colors": colors,
                "outcomes": outcomes
            }
