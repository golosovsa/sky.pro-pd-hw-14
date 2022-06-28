"""
    grm package
    database helper function
"""

# global imports
from dataclasses import dataclass, is_dataclass
import typing
import sqlite3

SQLITE_PREDICATES = ["", "AND", "OR"]
SQLITE_COMPARISON = {
    "equal": "= {}",
    "not_equal": "!= {}",
    "greater_that": "> {}",
    "greater_or_equal_that": ">= {}",
    "less_that": "< {}",
    "less_or_equal_that": "<= {}",
    "between": "BETWEEN {} AND {}",
    "not_between": "NOT BETWEEN {} AND {}",
    "in": "IN ({})",
}


def get_fields_query_from_dataclass(
        data_class: dataclass,
        aliases: typing.Union[None, typing.List[str], dataclass] = None) -> str:
    """ Get fields for sqlite query from dataclass

    :param data_class: Custom dataclass
    :param aliases: Column aliases
    :return: Part of sqlite query in a str type
    """

    if is_dataclass(data_class):
        if not aliases:
            return ", ".join([
                f"`{field}`"
                for field
                in data_class.__annotations__.keys()
            ])

        elif type(aliases) == list:
            return ", ".join([
                f"`{field}` AS `{alias}`"
                for field, alias
                in zip(data_class.__annotations__.keys(), aliases)
            ])

        elif is_dataclass(aliases):
            return ", ".join([
                f"`{field}` AS `{alias}`"
                for field, alias
                in zip(data_class.__annotations__.keys(), aliases.__annotations__.keys())
            ])

    raise TypeError(f"Wrong type parameters in function get_fields_query_from_dataclass\n"
                    f"Must be (data_class: dataclass, aliases: None | typing.List[str] | dataclass = None)\n"
                    f"You passed (data_class: {'dataclass' if is_dataclass(data_class) else type(data_class)}, "
                    f"aliases: {type(aliases)})")


class MakeVariable:

    def __init__(self, variable, value):
        self.name = variable
        self.value = value


class FieldName:

    def __init__(self, data_class):

        if not is_dataclass(data_class):
            raise TypeError("The data_class param must be a dataclass type")

        for attr in data_class.__annotations__.keys():
            setattr(self, attr, attr)


class Select:

    def __init__(self,
                 cursor: sqlite3.Cursor,
                 data_class: dataclass,
                 aliases: dataclass = None,
                 distinct=False):

        if not is_dataclass(data_class):
            raise TypeError(f"Param data_class must be a dataclass type, you passed a {type(data_class)} type.")

        if aliases is not None and not is_dataclass(aliases):
            raise TypeError(f"Param aliases must be a dataclass type, you passed a {type(aliases)} type.")

        self._cursor = cursor
        self.DataClass = aliases if aliases else data_class
        self._predicate = "SELECT DISTINCT" if distinct else "SELECT"
        self._query_fields = get_fields_query_from_dataclass(data_class, aliases)
        self._from_table = None
        self._filters = []
        self._filters_having = []
        self._group_by = []
        self._order_by = []
        self._limit = None
        self._offset = None
        self._query = None
        self._variables = {}
        self._auto_variable_index = 0
        self._auto_variable_part_of_name = "auto_var__"

    def from_table(self, table: str, alias: str = None) -> 'Select':

        if not table or type(table) != str:
            raise TypeError(f"param table must be a str type, you passed a {type(table)} type or empty.")

        if alias and type(alias) != str:
            raise TypeError(f"param alias must be a str type, you passed a {type(table)} type or empty.")

        self._from_table = f"{table} AS {alias}" if alias else table

    @staticmethod
    def _where_or_having(predicate: str, field: str, **kwargs) -> dict:

        if not field and type(field) is not str:
            raise TypeError(f"param field must be a str type, you passed a {type(field)} type or empty.")

        if not kwargs or len(kwargs) != 1:
            raise AttributeError("Must be one named parameter. Not more, not less.")

        comparison = list(kwargs.keys())[0]

        if comparison not in SQLITE_COMPARISON:
            raise AttributeError(f"Wrong keyword parameter.\n"
                                 f"Must be only one of them {SQLITE_COMPARISON.keys()}.\n"
                                 f"You passed {comparison}.")

        if type(predicate) != str or predicate not in SQLITE_PREDICATES:
            raise AttributeError(f"Wrong predicate parameter.\n"
                                 f"Must be only one of them {SQLITE_PREDICATES}.\n"
                                 f"You passed {predicate}.")

        return {'predicate': predicate, 'field': field, 'comparison': comparison, 'value': kwargs[comparison]}

    def where(self, field: str, **kwargs):
        self._filters.append(self._where_or_having("", field, **kwargs))
        return self

    def and_where(self, field: str, **kwargs):
        self._filters.append(self._where_or_having("AND", field, **kwargs))
        return self

    def or_where(self, field: str, **kwargs):
        self._filters.append(self._where_or_having("OR", field, **kwargs))
        return self

    def group_by(self, field):

        if not field and type(field) is not str:
            raise TypeError(f"param field must be a str type, you passed a {type(field)} type or empty.")

        self._group_by.append(field)

        return self

    def having(self, field: str, **kwargs):
        self._filters_having.append(self._where_or_having("", field, **kwargs))
        return self

    def and_having(self, field: str, **kwargs):
        self._filters_having.append(self._where_or_having("AND", field, **kwargs))
        return self

    def or_having(self, field: str, **kwargs):
        self._filters_having.append(self._where_or_having("OR", field, **kwargs))
        return self

    def order_by(self, field, desc=False):

        if not field and type(field) is not str:
            raise TypeError(f"param field must be a str type, you passed a {type(field)} type or empty.")

        self._order_by.append(f"{field} DESC" if desc else field)

        return self

    def limit(self, the_limit):

        if not the_limit and type(the_limit) is not int:
            raise TypeError(f"param the_limit must be a int type, you passed a {type(the_limit)} type or 0.")

        self._limit = the_limit

        return self

    def offset(self, the_offset):

        if not the_offset and type(the_offset) is not int:
            raise TypeError(f"param the_offset must be a int type, you passed a {type(the_offset)} type or 0.")

        self._offset = the_offset

        return self

    def _make_variable(self, variable: MakeVariable):

        if variable.name in self._variables:
            raise RuntimeError("The same name are already exist")

        self._variables[variable.name] = variable.value

    def _compile_add_param(self, param):

        value = param["value"]

        if type(value) == MakeVariable:
            self._make_variable(value)
            return f":{value.name}"

        if type(value) in (int, float):
            return str(value)

        if type(value) is str:
            variable = MakeVariable(f"{self._auto_variable_part_of_name}{self._auto_variable_index}")
            self._auto_variable_index += 1
            self._make_variable(variable)
            return f":{value.name}"

        if type(value) in (list, tuple):
            names = []
            for item in value:
                names.append(self._compile_add_param(item))
            return ", ".join(names)

        raise RuntimeError("Not supported type of value")

    def _compile_filter_or_having_make_comparison(self, comparison, value):

        # equal
        # not_equal
        # greater_that
        # greater_or_equal_that
        # less_that
        # less_or_equal_that
        # in
        if comparison not in ["between", "not_between"]:
            return SQLITE_COMPARISON[comparison].format(self._compile_add_param(value))

        # between
        # not_between
        if type(value) not in (list, tuple) or len(value) != 2:
            raise RuntimeError(f"The value for 'between' and 'not_between' "
                               f"must be a list or a tuple containing only 2 items.\n"
                               f"You passed {value}.")

        return SQLITE_COMPARISON[comparison].format(
            self._compile_add_param(value[0]),
            self._compile_add_param(value[1])
        )

    def _compile_filter_or_having(self,
                                  params: dict) -> str:

        if len(params) < 1:
            raise RuntimeError("Not enough params")

        if params[0].predicate != "":
            raise RuntimeError(f"First predicate in WITH or HAVING must be empty, you passed {params[0].predicate}")

        comparison = self._compile_filter_or_having_make_comparison(params[0].comparison, params[0].value)

        query = [f"{params[0].field} {comparison}"]

        for param in params[1:]:
            if params[0].predicate == "":
                raise RuntimeError(f"Params whats index is greater that 0 predicates\n"
                                   f"in WITH or HAVING must are {SQLITE_PREDICATES[1:]}."
                                   f"You passed {param.predicate}")

            comparison = self._compile_filter_or_having_make_comparison(param.comparison, param.value)
            query.append(f"{param.predicate} {param.field} {comparison}")

        return "\n".join(query)

    def compile(self):

        self._query = None

        if self._predicate is None or self._predicate == "" or \
                self._query_fields is None or self._query_fields == "" or \
                self._from_table is None or self._from_table == "":
            raise RuntimeError("Syntax error")

        base_query = f"{self._predicate} {self._query_fields} FROM {self._from_table}"

        filter_query = ""
        if len(self._filters) > 0:
            filter_query = f"\nWHERE {self._compile_filter_or_having(self._filters)}"

        group_by_query = ""
        if len(self._group_by) > 0:
            group_by_query = "\nGROUP BY" + ", ".join(self._group_by)

        having_query = ""
        if len(self._filters_having) > 0:
            having_query = f"\nHAVING {self._compile_filter_or_having(self._filters_having)}"

        order_by_query = ""
        if len(self._order_by) > 0:
            order_by_query = "\nORDER BY" + ", ".join(self._order_by)

        limit_query = ""
        if self._limit:
            limit_query = f"\nLIMIT {self._compile_add_param(self._limit)}"

        offset_query = ""
        if self._offset:
            offset_query = f"\nOFFSET {self._compile_add_param(self._offset)}"

        self._query = f"{base_query}" \
                      f"{filter_query}" \
                      f"{group_by_query}" \
                      f"{having_query}" \
                      f"{order_by_query}" \
                      f"{limit_query}" \
                      f"{offset_query}"

    def execute(self, cursor: sqlite3.Cursor = None):

        if cursor is None or type(cursor) != sqlite3.Cursor:
            cursor = self._cursor

        if self._query is None:
            self.compile()

        cursor.execute(self._query, self._variables)

        keys = [item[0] for item in cursor.description]
        result = []

        for row in cursor:
            data_class_params = dict(zip(keys, row))
            result.append(self.DataClass(**data_class_params))

        return result

