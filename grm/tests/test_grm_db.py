"""
    grm package
    testing database helper functions
"""


# global imports
from dataclasses import dataclass
import pytest


# local imports
import pytest

from ..db import get_fields_query_from_dataclass, MakeVariable, FieldName


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

    def test_field_name_wrong_type(self):

        with pytest.raises(TypeError):
            names = FieldName(3.14)
            names = FieldName("3.14")
            names = FieldName(314)
            names = FieldName(object)
            names = FieldName(None)
