from steps.config import Config
from behave import *


def before_all(context):
    context.config = Config()


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
