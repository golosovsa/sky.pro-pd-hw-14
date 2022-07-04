import random
import sqlite3


def make_rows(count):
    result = []

    for i in range(count):
        show_id = f"s{i}"
        type_ = f"type{random.randint(1, 2)}"
        title = f"title{i}"

        director = ", ".join([f"director{random.randint(1, 10)}" for _ in range(random.randint(2, 4))]) \
            if random.randint(1, 5) == 1 \
            else f"director{random.randint(1, 10)}"
        cast = ", ".join([f"actor{random.randint(1, 20)}" for _ in range(random.randint(3, 6))])
        country = ", ".join([f"country{random.randint(1, 5)}" for _ in range(random.randint(2, 3))]) \
            if random.randint(1, 5) == 1 \
            else f"country{random.randint(1, 5)}"
        date_added = sqlite3.Date(2010 + random.randint(-10, 10), random.randint(1, 12), random.randint(1, 28))
        release_year = 2010 + random.randint(-10, 10)
        rating = f"rating{random.randint(1, 4)}"
        duration = random.randint(200, 500) if type_ == "type1" else random.randint(1, 12)
        duration_type = f"duration{type_}"
        listed_in = ", ".join([f"genre{random.randint(1, 5)}" for _ in range(random.randint(2, 5))]) \
            if random.randint(1, 5) == 1 \
            else f"genre{random.randint(1, 5)}"
        description = f"description{i}"

        result.append([show_id,
                       type_,
                       title,
                       director,
                       cast,
                       country,
                       date_added,
                       release_year,
                       rating,
                       duration,
                       duration_type,
                       listed_in,
                       description,
                       ])

    for i in range(13):
        for j in range(random.randint(1, 5)):
            index = random.randint(0, count - 1)
            result[index][i] = None

    for i in range(count):
        for j in range(len(result[i])):
            if type(result[i][j]) not in (str, int):
                result[i][j] = str(result[i][j])

    for i in range(count):
        result[i] = tuple(result[i])

    return result

result = make_rows(100)
print(result)