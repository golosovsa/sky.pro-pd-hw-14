"""
    GRM package
    Database helper functions
"""


# global imports
from dataclasses import fields


def get_fields_str_from_dataclass(data_class):

    result = []

    for field in fields(data_class):

        if "column" in field.metadata:
            result.append(f"`{field.metadata['column']}` AS `{field.name}`")

        elif "table.column" in field.metadata:
            result.append(f"{field.metadata['table.column']} AS `{field.name}`")

        else:
            result.append(f"`{field.name}`")

    return  ", ".join(result)


def get_fields_str_for_sqlite_json_function(data_class):

    result = []

    for field in fields(data_class):

        result.append(f"'{field.name}'")

        if "column" in field.metadata:
            result.append(f"`{field.metadata['column']}`")

        elif "table.column" in field.metadata:
            result.append(field.metadata['table.column'])

        else:
            result.append(f"`{field.name}`")

    return ", ".join(result)
