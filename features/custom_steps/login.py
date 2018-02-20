from behave import *
from steps.biblioteca.api import Api


@given(u'que eu quero executar o login')
def step_impl(context):
    context.api = Api()


@when(u'eu tento executar o login')
def step_impl(context):
    # print("parameters=%s\n" % context.api.parameters)
    context.api.url(context.config.base_url + 'login')
    context.api.post()
