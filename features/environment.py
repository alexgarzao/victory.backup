from steps.config import Config
from behave import *
from steps.biblioteca.api import Api


def before_all(context):
    context.config = Config()


def before_feature(context, feature):
    # import pdb; pdb.set_trace()
    if 'setup' in feature.tags:
        return

    api = Api()
    api.url(context.config.base_url + 'bdd-init')
    api.post()
    api.validar_retorno(204)


#def before_step(context, step):
#    import time; time.sleep(0.1)



# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type

import parse
import parse_type


# @parse.with_pattern(r"\d+")
def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
register_type(Number=parse_number)
