from steps.fields import Fields
from steps.http_status_codes import HttpStatusCodes
from steps.biblioteca.global_data import GlobalData


class Config():
    def __init__(self):
        self.fields = Fields()
        self.http_status_codes = HttpStatusCodes()
        self.global_data = GlobalData()
        self.base_url = ''
