"""
    GRM package
    Factories
"""


# SQLite factories


def do_sqlite_dict_factory(cursor, row):
    """ Serialize fetched data, Row factory.  """
    result = {}
    for idx, col in enumerate(cursor.description):
        result[col[0]] = row[idx]
    return result
