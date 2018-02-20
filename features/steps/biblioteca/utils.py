import json


def assert_equal(context, result, expected_result, custom_message):

    expected_result = context.config.global_data.get_content(expected_result)

    if expected_result == 'sim':
        expected_result = True
        message = custom_message + ' recebido "%s" difere do esperado "%s"'
        assert result == expected_result, message % (result, expected_result)
    elif expected_result == u'não':
        expected_result = False
        message = custom_message + ' recebido "%s" difere do esperado "%s"'
        assert result == expected_result, message % (result, expected_result)
    elif expected_result == '<nulo>':
        expected_result = None
        message = custom_message + ' recebido "%s" difere do esperado "%s"'
        assert result == expected_result, message % (result, expected_result)
    elif expected_result == '<nao nulo>':
        expected_result = None
        message = custom_message + ' recebido "%s" difere do esperado not "%s"'
        assert result != expected_result, message % (result, expected_result)
    elif expected_result == '<vazio>':
        expected_result = u''
        message = custom_message + ' recebido "%s" difere do esperado "%s"'
        assert result == expected_result, message % (result, expected_result)
    elif expected_result == '<nao vazio>':
        expected_result = u''
        message = custom_message + ' recebido "%s" difere do esperado not "%s"'
        assert result != expected_result, message % (result, expected_result)
    else:
        message = custom_message + ' recebido "%s" difere do esperado "%s"'
        assert result == expected_result or str(result) == expected_result, message % (result, expected_result)


def define_value(context, value):
    defined_value = context.config.global_data.get_content(value)
    return parse_value(defined_value)


def define_list_value(context, value):
    value = parse_value(value)
    if not value:
        return []

    return [int(x) if __is_valid(x) else define_value(context, x.strip()) for x in value]


def __is_valid(value):
    return (isinstance(value, str) and value.isdigit()) or isinstance(value,int)


def parse_value(value):
    if type(value) == str and value == '<nulo>':
        value = None
    elif type(value) == str and value == '<vazio>':
        value = ""
    elif type(value) == str and value == u'não':
        value = False
    elif type(value) == str and value == 'sim':
        value = True
    return value


def assert_condition(context, condition, custom_message):
    message = custom_message + ' condicao falhou'
    assert condition, message


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def deep_find(values, key_to_find, value=None):
    result_list = deep_search(values, key_to_find)
    return value in result_list


def deep_search(values, key_to_find):
    result_list = []

    for key, value in values.items():
        if type(value) == dict:
            r = deep_search(value, key_to_find)
            if r:
                result_list += r

        if key == key_to_find:
            result_list.append(value)
            continue

    return sorted(result_list)


def check_list_table_result(context, api_result, field_list):
    assert_equal(context, len(api_result), len(context.table.rows), 'Numero de registros')

    for row_index in range(0, len(context.table.rows)):
        # print ('### Linha da tabela: ', row_index+1)
        row_api_result = api_result[row_index]
        row_expected_result = context.table[row_index]

        for field_index in range(0, len(field_list)):
            field = field_list[field_index]
            field_print_name, field_name = field

            field_api_result = row_api_result[field_name]
            field_expected_result = row_expected_result[field_index]
            field_expected_result = define_value(context, field_expected_result)
            field_expected_result_str = str(row_expected_result[field_index])

            if type(field_api_result) == list and len(field_api_result) == 0:
                field_api_result = []

            if type(field_api_result) == set and len(field_api_result) == 0:
                field_api_result = set([])

            if type(field_api_result) == list:
                if field_expected_result != None and field_expected_result != '':
                    field_expected_result_str = field_expected_result.split(',')
                    field_expected_result = [int(x) if x.isdigit() else x for x in field_expected_result_str]
                else:
                    field_expected_result = []

            if type(field_api_result) == set:
                if field_expected_result != '<vazio>' and field_expected_result != '<nulo>':
                    field_expected_result_str = set(field_expected_result.split(','))
                    field_expected_result = [int(x) if x.isdigit() else x for x in field_expected_result_str]
                else:
                    field_expected_result = set([])

            if field_api_result != None:
                field_api_result = str(field_api_result)

            if field_expected_result != None:
                field_expected_result = str(field_expected_result)

            if str(field_api_result) != str(field_expected_result) and str(field_api_result) != str(field_expected_result_str):
                assert_equal(context, field_api_result, str(field_expected_result) + " ou " + field_expected_result_str, field_print_name)


def pretty_json(json_values):
    return json.dumps(json_values, indent=4, sort_keys=True, separators=(',', ': '))
