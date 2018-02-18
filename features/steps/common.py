from behave import *
from biblioteca.utils import define_value, assert_equal, parse_value


@then(u'obtenho a lista de dados abaixo')
def step_impl(context):
    api_result = context.api.retorno.json()
    valida_lista_dados(context, api_result)


def valida_lista_dados(context, api_result):
    expected_columns = context.table.headings
    for row_index in range(0, len(context.table.rows)):
        if row_index >= len(context.table.rows) or row_index >= len(api_result):
            break

        row_api_result = api_result[row_index]
        row_expected_result = context.table[row_index]

        # print ("#### Linha tabela: ", row_index + 1)

        current_column = 0
        for expected_column in expected_columns:
            expected_result = row_expected_result[current_column]
            current_column += 1

            object_name, alias = __split_name(expected_column)

            # Se eh um objeto, mas o esperado para o objeto eh nulo, entao ignoramos o valor que os campos tem.
            if object_name in expected_columns and row_expected_result[expected_columns.index(object_name)] == '<nulo>':
                assert_equal(context, row_api_result[object_name], '<nulo>', expected_column)
                continue

            # TODO: acho que o alias poderia indicar o objeto tambem.
            field = context.config.fields.get_field(alias)
            assert field != None, 'Alias %s nao encontrado' % alias
            field_name = field.json_name

            if not object_name:
                row_api_value = row_api_result[field_name]
            else:
                row_api_value = row_api_result[object_name][field_name]

            #TODO Esta verificação de lista funciona somente para inteiros. Precisa de refactor.
            if isinstance(row_api_value, list):
                expected_result = parse_value(expected_result)

                if expected_result == None:
                    expected_result = []
                else:
                    expected_result_splited = expected_result.split(',')
                    expected_result = [int(x) if x.isdigit() else define_value(context, x.strip()) for x in expected_result_splited]

            # Valida o conteudo do campo do objeto.
            assert_equal(context, row_api_value, expected_result, expected_column)

    assert_equal(context, len(api_result), len(context.table.rows), 'Numero de registros')

def __split_name(name):
    dot_position = name.find('.')
    if dot_position == -1:
        return None, name

    object_name = name[:dot_position]
    field_name = name[dot_position+1:]
    return object_name, field_name


@then(u'obtenho uma lista vazia')
def step_impl(context):
    api_result = context.api.retorno.json()
    assert_equal(context, len(api_result), 0, 'Zero registros')
