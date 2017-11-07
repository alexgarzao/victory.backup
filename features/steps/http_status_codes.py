class HttpStatusCode(object):
    def __init__(self, alias, status_code):
        self.alias = alias
        self.status_code = status_code


class HttpStatusCodes(object):
    def __init__(self):
        self.__http_status_code_list = {}

    def new_alias(self, alias, status_code):
        self.__http_status_code_list[alias] = HttpStatusCode(alias, status_code)

    def get_code(self, alias):
        return self.__http_status_code_list[alias].status_code
