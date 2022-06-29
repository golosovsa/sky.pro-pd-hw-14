"""
    grm package
    testing database helper functions
"""

# global imports
from dataclasses import dataclass, astuple
import pytest

# local imports
import pytest

from ..db import get_fields_query_from_dataclass, MakeVariable, FieldName, Select


@pytest.fixture
def test_data_class_type_fixture_1():
    @dataclass
    class TestDataClass:
        field1: str = "12345"
        field2: int = 1234
        field3: float = 1.234
        field4: bool = True
        field5: str = None

    return TestDataClass


@pytest.fixture
def test_data_class_type_fixture_2():
    @dataclass
    class TestDataClass:
        _field1_: str = "12345"
        _field2_: int = 1234
        _field3_: float = 1.234
        _field4_: bool = True
        _field5_: str = None

    return TestDataClass


@pytest.fixture
def test_data_class_instance_fixture_1():
    @dataclass
    class TestDataClass:
        field1: str = "12345"
        field2: int = 1234
        field3: float = 1.234
        field4: bool = True
        field5: str = None

    return TestDataClass()


@pytest.fixture
def test_data_class_instance_fixture_2():
    @dataclass
    class TestDataClass:
        _field1_: str = "12345"
        _field2_: int = 1234
        _field3_: float = 1.234
        _field4_: bool = True
        _field5_: str = None

    return TestDataClass()


@pytest.fixture
def test_data_class_all_columns():
    @dataclass
    class TestAllColumns:
        show_id: str = None
        type: str = None
        title: str = None
        director: str = None
        cast: str = None
        country: str = None
        date_added: int = None
        release_year: str = None
        rating: str = None
        duration: int = None
        duration_type: str = None
        listed_in: str = None
        description: str = None

    return TestAllColumns


@pytest.fixture
def test_data_class_all_columns_aliases():
    @dataclass
    class TestAllColumnsAliases:
        field1: str = None
        field2: str = None
        field3: str = None
        field4: str = None
        field5: str = None
        field6: str = None
        field7: int = None
        field8: str = None
        field9: str = None
        field10: int = None
        field11: str = None
        field12: str = None
        field13: str = None

    return TestAllColumnsAliases


@pytest.fixture
def test_data_class_two_columns_1():

    @dataclass
    class TestTwoColumns:
        title: str
        release_year: int

    return TestTwoColumns


@pytest.fixture
def test_data_class_two_columns_2():

    @dataclass
    class TestTwoColumns:
        title: str
        type: str
        count_in_group: int

    return TestTwoColumns


@pytest.fixture
def test_data_class_three_columns_1():

    @dataclass
    class TestTwoColumns:
        title: str
        release_year: int
        count_in_group: int

    return TestTwoColumns


class TestGRMDB:

    def test_get_fields_query_from_dataclass_type(self, test_data_class_type_fixture_1):
        fields_query = get_fields_query_from_dataclass(test_data_class_type_fixture_1)

        assert "field1" in fields_query, "Something wrong, must be True"
        assert "field2" in fields_query, "Something wrong, must be True"
        assert "field3" in fields_query, "Something wrong, must be True"
        assert "field4" in fields_query, "Something wrong, must be True"
        assert "field5" in fields_query, "Something wrong, must be True"

        assert "`field1`, `field2`, `field3`, `field4`, `field5`" == fields_query, "Something wrong, must be equal"

    def test_get_fields_query_from_dataclass_instance(self, test_data_class_instance_fixture_1):
        fields_query = get_fields_query_from_dataclass(test_data_class_instance_fixture_1)

        assert "field1" in fields_query, "Something wrong, must be True"
        assert "field2" in fields_query, "Something wrong, must be True"
        assert "field3" in fields_query, "Something wrong, must be True"
        assert "field4" in fields_query, "Something wrong, must be True"
        assert "field5" in fields_query, "Something wrong, must be True"

        assert "`field1`, `field2`, `field3`, `field4`, `field5`" == fields_query, "Something wrong, must be equal"

    def test_get_fields_query_from_wrong_type(self):
        with pytest.raises(TypeError):
            fields_query = get_fields_query_from_dataclass(None)
            fields_query = get_fields_query_from_dataclass(12345)
            fields_query = get_fields_query_from_dataclass("12345")
            fields_query = get_fields_query_from_dataclass(1.2345)

    def test_get_fields_query_from_dataclass_type_with_aliases_list(
            self,
            test_data_class_type_fixture_1,
            test_data_class_type_fixture_2
    ):
        aliases = list(test_data_class_type_fixture_2.__annotations__.keys())

        fields_query = get_fields_query_from_dataclass(test_data_class_type_fixture_1, aliases)

        assert "field1" in fields_query, "Something wrong, must be True"
        assert "field2" in fields_query, "Something wrong, must be True"
        assert "field3" in fields_query, "Something wrong, must be True"
        assert "field4" in fields_query, "Something wrong, must be True"
        assert "field5" in fields_query, "Something wrong, must be True"

        assert "_field1_" in fields_query, "Something wrong, must be True"
        assert "_field2_" in fields_query, "Something wrong, must be True"
        assert "_field3_" in fields_query, "Something wrong, must be True"
        assert "_field4_" in fields_query, "Something wrong, must be True"
        assert "_field5_" in fields_query, "Something wrong, must be True"

        assert "`field1` AS `_field1_`, `field2` AS `_field2_`, `field3` AS `_field3_`, " \
               "`field4` AS `_field4_`, `field5` AS `_field5_`" == fields_query, \
            "Something wrong, must be equal"

    def test_get_fields_query_from_dataclass_type_with_aliases_dataclass(
            self,
            test_data_class_type_fixture_1,
            test_data_class_type_fixture_2
    ):
        fields_query = get_fields_query_from_dataclass(
            test_data_class_type_fixture_1,
            test_data_class_type_fixture_2
        )

        assert "field1" in fields_query, "Something wrong, must be True"
        assert "field2" in fields_query, "Something wrong, must be True"
        assert "field3" in fields_query, "Something wrong, must be True"
        assert "field4" in fields_query, "Something wrong, must be True"
        assert "field5" in fields_query, "Something wrong, must be True"

        assert "_field1_" in fields_query, "Something wrong, must be True"
        assert "_field2_" in fields_query, "Something wrong, must be True"
        assert "_field3_" in fields_query, "Something wrong, must be True"
        assert "_field4_" in fields_query, "Something wrong, must be True"
        assert "_field5_" in fields_query, "Something wrong, must be True"

        assert "`field1` AS `_field1_`, `field2` AS `_field2_`, `field3` AS `_field3_`, " \
               "`field4` AS `_field4_`, `field5` AS `_field5_`" == fields_query, \
            "Something wrong, must be equal"

    def test_make_variable(self):
        variable = MakeVariable("name", "value")

        assert hasattr(variable, "name"), "Must have a name attribute"
        assert hasattr(variable, "value"), "Must have a value attribute"

        assert variable.name == "name", "Must be equal"
        assert variable.value == "value", "Must be equal"

    def test_field_name(self, test_data_class_type_fixture_1):
        names = FieldName(test_data_class_type_fixture_1)

        assert hasattr(names, "field1"), "Must have attribute"
        assert hasattr(names, "field2"), "Must have attribute"
        assert hasattr(names, "field3"), "Must have attribute"
        assert hasattr(names, "field4"), "Must have attribute"
        assert hasattr(names, "field5"), "Must have attribute"

        assert names.field1 == "field1", "Must be equal"
        assert names.field2 == "field2", "Must be equal"
        assert names.field3 == "field3", "Must be equal"
        assert names.field4 == "field4", "Must be equal"
        assert names.field5 == "field5", "Must be equal"

    def test_field_name_by_index(self, test_data_class_type_fixture_1):
        names = FieldName(test_data_class_type_fixture_1)

        assert names.get_column_by_index(0) == "field1", "Must be equal"
        assert names.get_column_by_index(1) == "field2", "Must be equal"
        assert names.get_column_by_index(2) == "field3", "Must be equal"
        assert names.get_column_by_index(3) == "field4", "Must be equal"
        assert names.get_column_by_index(4) == "field5", "Must be equal"

    def test_field_name_wrong_type(self):
        with pytest.raises(TypeError):
            names = FieldName(3.14)
            names = FieldName("3.14")
            names = FieldName(314)
            names = FieldName(object)
            names = FieldName(None)

    def test_select_class_from_table(self, test_db_cursor, test_data_class_all_columns):

        select = Select(test_db_cursor, test_data_class_all_columns).from_table("netflix")

        select.compile()

        assert "SELECT" in select._query, "Must include SELECT"
        assert "FROM" in select._query, "Must include FROM"
        assert "netflix" in select._query, "Must include 'netflix'"

        result = select.execute()

        assert len(result) == 7787, "Must be equal"
        assert type(result[0]) is test_data_class_all_columns, "Must be instance of"

        for value in astuple(result[0]):
            assert value is not None, "Must be not None"

    def test_select_class_from_table_field_aliases(self,
                                                   test_db_cursor,
                                                   test_data_class_all_columns,
                                                   test_data_class_all_columns_aliases):
        select = Select(test_db_cursor,
                        test_data_class_all_columns,
                        aliases=test_data_class_all_columns_aliases).from_table("netflix")

        select.compile()

        assert "`show_id` AS `field1`" in select._query, "Must be include"
        assert "`type` AS `field2`" in select._query, "Must be include"
        assert "`title` AS `field3`" in select._query, "Must be include"
        assert "`director` AS `field4`" in select._query, "Must be include"
        assert "`cast` AS `field5`" in select._query, "Must be include"
        assert "`country` AS `field6`" in select._query, "Must be include"
        assert "`date_added` AS `field7`" in select._query, "Must be include"
        assert "`release_year` AS `field8`" in select._query, "Must be include"
        assert "`rating` AS `field9`" in select._query, "Must be include"
        assert "`duration` AS `field10`" in select._query, "Must be include"
        assert "`duration_type` AS `field11`" in select._query, "Must be include"
        assert "`listed_in` AS `field12`" in select._query, "Must be include"
        assert "`description` AS `field13`" in select._query, "Must be include"

        result = select.execute()

        assert len(result) == 7787, "Must be equal"
        assert type(result[0]) is test_data_class_all_columns_aliases, "Must be instance of"

    def test_select_class_from_table_table_alias(self,
                                                 test_db_cursor,
                                                 test_data_class_all_columns):
        select = Select(test_db_cursor,
                        test_data_class_all_columns).from_table("netflix", "test_table")

        select.compile()

        assert "netflix AS test_table" in select._query, "Must be include"

    def test_select_class_where_all_only_null(self, test_db_cursor, test_data_class_all_columns):

        select = Select(test_db_cursor, test_data_class_all_columns)\
            .from_table("netflix").where(FieldName(test_data_class_all_columns).show_id, only_null=True)

        for field in list(test_data_class_all_columns.__annotations__.keys())[1:]:
            select.and_where(field, only_null=True)

        select.compile()

        assert "WHERE" in select._query, "Must be include"

        assert "`show_id` IS NULL" in select._query, "Must be include"
        assert "AND `type` IS NULL" in select._query, "Must be include"
        assert "AND `title` IS NULL" in select._query, "Must be include"
        assert "AND `director` IS NULL" in select._query, "Must be include"
        assert "AND `cast` IS NULL" in select._query, "Must be include"
        assert "AND `country` IS NULL" in select._query, "Must be include"
        assert "AND `date_added` IS NULL" in select._query, "Must be include"
        assert "AND `release_year` IS NULL" in select._query, "Must be include"
        assert "AND `rating` IS NULL" in select._query, "Must be include"
        assert "AND `duration` IS NULL" in select._query, "Must be include"
        assert "AND `duration_type` IS NULL" in select._query, "Must be include"
        assert "AND `listed_in` IS NULL" in select._query, "Must be include"
        assert "AND `description` IS NULL" in select._query, "Must be include"

        result = select.execute()

        assert len(result) == 0, "Must be empty"

    def test_select_class_where_any_only_null(self, test_db_cursor, test_data_class_all_columns):

        select = Select(test_db_cursor, test_data_class_all_columns)\
            .from_table("netflix").where(FieldName(test_data_class_all_columns).show_id, only_null=True)

        for field in list(test_data_class_all_columns.__annotations__.keys())[1:]:
            select.or_where(field, only_null=True)

        select.compile()

        assert "`show_id` IS NULL" in select._query, "Must be include"
        assert "OR `type` IS NULL" in select._query, "Must be include"
        assert "OR `title` IS NULL" in select._query, "Must be include"
        assert "OR `director` IS NULL" in select._query, "Must be include"
        assert "OR `cast` IS NULL" in select._query, "Must be include"
        assert "OR `country` IS NULL" in select._query, "Must be include"
        assert "OR `date_added` IS NULL" in select._query, "Must be include"
        assert "OR `release_year` IS NULL" in select._query, "Must be include"
        assert "OR `rating` IS NULL" in select._query, "Must be include"
        assert "OR `duration` IS NULL" in select._query, "Must be include"
        assert "OR `duration_type` IS NULL" in select._query, "Must be include"
        assert "OR `listed_in` IS NULL" in select._query, "Must be include"
        assert "OR `description` IS NULL" in select._query, "Must be include"

        result = select.execute()

        assert len(result) == 11, "Must be 11"

    def test_select_class_where_field_equal(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, equal=2000)

        result = select.execute()

        for row in result:
            assert row.release_year == 2000, "Must be equal"

        assert len(result) == 34, "Must be 34"

    def test_select_class_where_field_not_equal(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, not_equal=2000)

        result = select.execute()

        for row in result:
            assert row.release_year != 2000, "Must be not equal"

        assert len(result) == 7753, "Must be 7753"

    def test_select_class_where_field_greater_that(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, greater_that=2000)

        result = select.execute()

        for row in result:
            assert row.release_year > 2000, "Must be greater"

        assert len(result) == 7304, "Must be 7304"

    def test_select_class_where_field_greater_or_equal_that(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, greater_or_equal_that=2000)

        result = select.execute()

        for row in result:
            assert row.release_year >= 2000, "Must be greater or equal"

        assert len(result) == 7338, "Must be 7338"

    def test_select_class_where_field_less_that(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, less_that=2000)

        result = select.execute()

        for row in result:
            assert row.release_year < 2000, "Must be less"

        assert len(result) == 449, "Must be 449"

    def test_select_class_where_field_less_or_equal_that(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, less_or_equal_that=2000)

        result = select.execute()

        for row in result:
            assert row.release_year <= 2000, "Must be less or equal"

        assert len(result) == 483, "Must be 483"

    def test_select_class_where_field_between(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, between=(2000, 2001))

        result = select.execute()

        for row in result:
            assert 2000 <= row.release_year <= 2001, "Must be in interval"

        assert len(result) == 70, "Must be 70"

    def test_select_class_where_field_not_between(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, not_between=(2000, 2001))

        result = select.execute()

        for row in result:
            assert row.release_year > 2001 or row.release_year < 2000, "Must be not in interval"

        assert len(result) == 7717, "Must be 7717"

    def test_select_class_where_field_in(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).release_year, in_the=(2000, 2010))
        result = select.execute()

        for row in result:
            assert row.release_year == 2000 or row.release_year == 2010, "Must be equal"

        assert len(result) == 207, "Must be 207"

    def test_select_class_where_like(self, test_db_cursor, test_data_class_two_columns_1):

        select = Select(test_db_cursor, test_data_class_two_columns_1).from_table("netflix")\
            .where(FieldName(test_data_class_two_columns_1).title, like="%train%")

        result = select.execute()

        for row in result:
            assert "train" in row.title.lower(), "Must be include"

        assert len(result) == 9, "Must be 9"

    def test_select_class_group_by(self, test_db_cursor, test_data_class_two_columns_2):

        select = Select(test_db_cursor, test_data_class_two_columns_2)\
            .make_aggregate(FieldName(test_data_class_two_columns_2).count_in_group, count="*")\
            .from_table("netflix")\
            .group_by(FieldName(test_data_class_two_columns_2).type)

        select.compile()

        assert "COUNT(*) AS `count_in_group`" in select._query, "Must include"
        assert "GROUP BY " in select._query, "Must include"

        result = select.execute()

        assert len(result) == 2, "must be equal"

        assert result[0].count_in_group == 5377, "Must be 5377"
        assert result[0].type == "Movie"
        assert result[1].count_in_group == 2410, "Must be 2410"
        assert result[1].type == "TV Show"

    def test_select_class_group_by_distinct(self, test_db_cursor, test_data_class_two_columns_2):

        select = Select(test_db_cursor, test_data_class_two_columns_2)\
            .make_aggregate(FieldName(test_data_class_two_columns_2).count_in_group,
                            distinct=True,
                            count=FieldName(test_data_class_two_columns_2).type)\
            .from_table("netflix")\
            .group_by(FieldName(test_data_class_two_columns_2).type)

        select.compile()

        assert "COUNT(DISTINCT `type`) AS `count_in_group`" in select._query, "Must include"
        assert "GROUP BY " in select._query, "Must include"

        result = select.execute()

        assert len(result) == 2, "must be equal"

        assert result[0].count_in_group == 1, "Must be 1"
        assert result[0].type == "Movie"
        assert result[1].count_in_group == 1, "Must be 1"
        assert result[1].type == "TV Show"

    def test_select_class_having(self, test_db_cursor, test_data_class_three_columns_1):

        select = Select(test_db_cursor, test_data_class_three_columns_1) \
            .make_aggregate(FieldName(test_data_class_three_columns_1).count_in_group,
                            count="*") \
            .from_table("netflix") \
            .group_by(FieldName(test_data_class_three_columns_1).release_year)\
            .having(FieldName(test_data_class_three_columns_1).count_in_group, greater_that=100)

        select.compile()

        assert "HAVING " in select._query, "Must include"

        result = select.execute()

        assert len(result) == 13, "Must be 13"

        for row in result:
            assert row.count_in_group > 100, "Must be greater"

    def test_select_class_sort_by(self, test_db_cursor, test_data_class_two_columns_1):
        select = Select(test_db_cursor, test_data_class_two_columns_1) \
            .from_table("netflix") \
            .order_by(FieldName(test_data_class_two_columns_1).release_year)

        select.compile()

        assert "ORDER BY " in select._query, "Must include"

        result = select.execute()

        assert len(result) == 7787, "Must be 7787"

        prev = result[0].release_year

        for row in result:
            assert prev <= row.release_year
            prev = row.release_year

    def test_select_class_sort_by_desc(self, test_db_cursor, test_data_class_two_columns_1):
        select = Select(test_db_cursor, test_data_class_two_columns_1) \
            .from_table("netflix") \
            .order_by(FieldName(test_data_class_two_columns_1).release_year, desc=True)

        select.compile()

        assert "ORDER BY " in select._query, "Must include"

        result = select.execute()

        assert len(result) == 7787, "Must be 7787"

        prev = result[0].release_year

        for row in result:
            assert prev >= row.release_year
            prev = row.release_year

