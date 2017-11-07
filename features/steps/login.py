from behave import *
from steps.biblioteca.api import Api


# TODO: poder configurar a URL no SETUP
API_BASE_URL = 'http://localhost:5000/'

@given(u'que eu quero executar o login')
def step_impl(context):
    context.api = Api()


@when(u'eu tento executar o login')
def step_impl(context):
    print("parameters=%s\n" % context.api.parameters)
    context.api.url(API_BASE_URL + 'login')
    context.api.post()
