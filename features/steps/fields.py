from enum import IntEnum, unique
from steps.biblioteca.utils import is_float


@unique
class FieldType(IntEnum):
    STRING = 1
    INTEGER = 2
    NUMBER = 3
    BOOL = 4
    DATE = 5
    STRING_LIST = 6
    INTEGER_LIST = 7


# TODO: Esta classe poderia se especializada conforme o tipo.
# Assim poderiamos remover os if's abaixo.
class Field(object):
    def __init__(self, alias, type, json_name):
        self.alias = alias
        self.type = FieldType[type.upper()]
        self.json_name = json_name
        self.value = None

    def set_value(self, value):
        if self.type == FieldType.STRING:
            self.value = self.__get_string_value(value)
        elif self.type == FieldType.INTEGER:
            self.value = self.__get_integer_value(value)
        elif self.type == FieldType.NUMBER:
            self.value = self.__get_number_value(value)
        elif self.type == FieldType.BOOL:
            self.value = self.__get_bool_value(value)
        elif self.type == FieldType.STRING_LIST:
            self.value = self.__get_string_list_value(value)
        else:
            assert False, 'FieldType indefinido!'

    def __get_string_value(self, value):
        # Verifica se tem " ou ' para serem retirados
        if len(value) >= 2:
            if value[0] == '\'' and value[len(value)-1] == '\'' or \
                value[0] == '"' and value[len(value)-1] == '"':
                value = value[1:-1]
        return value

    def __get_integer_value(self, value):
        if value == '<nulo>':
            return None

        if value.isdigit():
            return int(value)

        return value

    def __get_number_value(self, value):
        if value == '<nulo>':
            return None

        if is_float(value):
            return float(value)

        return value

    def __get_bool_value(self, value):
        if value == '<nulo>':
            return None

        return value.upper() == 'SIM'

    def __get_string_list_value(self, value):
        if value == '<vazio>':
            return []

        if value == '<nulo>':
            return None

        return value.split(',')

    def get_value(self):
        return self.value


class Fields(object):
    def __init__(self):
        self.__field_list = {}

    def new_field(self, name, type, json_name):
        self.__field_list[name] = Field(name, type, json_name)

    def get_field(self, alias):
        return self.__field_list.get(alias)
