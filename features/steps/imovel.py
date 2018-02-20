from behave import *
from steps.biblioteca.api import Api


# TODO: Estes steps deveriam ser configuraveis.

@given(u'que eu quero cadastrar um imóvel')
def step_impl(context):
    context.api = Api()


@when(u'eu tento cadastrar o imóvel')
def step_impl(context):
    context.api.url(context.config.base_url + 'imoveis')
    context.api.post()


@given(u'que eu quero listar os meus imóveis')
def step_impl(context):
    context.api = Api()


@when(u'eu busco a lista de imóveis')
def step_impl(context):
    context.api.url(context.config.base_url + 'imoveis')
    context.api.get()
