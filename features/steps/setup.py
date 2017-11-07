from behave import *


@given(u'que eu quero mapear os campos do JSON')
def step_impl(context):
    pass


@given(u'o campo {alias} é do tipo {type} e corresponde ao {field} no JSON')
def step_impl(context, alias, type, field):
    context.config.fields.new_field(alias, type, field)


@when(u'eu tento mapear os campos')
def step_impl(context):
    pass


@then(u'nenhuma falha ocorre')
def step_impl(context):
    pass


@given(u'que eu quero mapear os códigos de retorno do HTTP')
def step_impl(context):
    pass


@given(u'o código {http_status_code:Number} indica {alias}')
def step_impl(context, http_status_code, alias):
    context.config.http_status_codes.new_alias(alias, http_status_code)


@when(u'eu tento mapear os códigos de retorno')
def step_impl(context):
    pass


@then(u'eu recebo o status que indica {alias}')
def step_impl(context, alias):
    http_status_code = context.config.http_status_codes.get_code(alias)
    context.api.validar_retorno(http_status_code)


@given(u'o campo {alias} é {value}')
def step_impl(context, alias, value):
    field = context.config.fields.get_field(alias)
    assert field != None, 'Alias %s nao encontrado' % alias
    field.set_value(value)
    context.api.parameters[field.json_name] = field.get_value()
