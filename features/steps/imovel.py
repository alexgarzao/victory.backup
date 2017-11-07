from behave import *
from steps.biblioteca.api import Api


@given(u'que eu quero cadastrar um imóvel')
def step_impl(context):
    context.api = Api()


@when(u'eu tento cadastrar o imóvel')
def step_impl(context):
    # TODO: poder configurar a URL no SETUP
    context.api.url('http://localhost:5000/imoveis')
    context.api.post()


@given(u'que eu quero listar os meus imóveis')
def step_impl(context):
    context.api = Api()


@when(u'eu busco a lista de imóveis')
def step_impl(context):
    # TODO: poder configurar a URL no SETUP
    context.api.url('http://localhost:5000/imoveis')
    context.api.get()
