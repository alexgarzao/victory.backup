import json
import requests
import logging
from .utils import deep_find, deep_search, pretty_json


class Api(object):
    def __init__(self):
        self.last_parameters = None
        self.retorno = None
        self.parameters = {}

    def url(self, url):
        # logging.info("URL: " + url)
        self.url = url

    def get(self):
        try:
            url = self.url
            self.last_parameters = {}
            self.retorno = requests.get(url)
            return self.retorno
        except Exception as e:
            raise e

    def post(self):
        try:
            # print ("Api Post")
            url = self.url
            # print (" URL:" + self.url)
            self.last_parameters = self.parameters
            self.retorno = requests.post(url, json=self.parameters)
            # if self.success():
            #     print ("POST OK: ", self.url, self.last_parameters)
            # else:
            #     print ("POST NOK: ", self.url, self.last_parameters)
            # print ("Api Post Concluido")
            return self.retorno
        except Exception as e:
            raise e

    def post_image(self, caminho_imagem):
        try:
            # print ("Api Post Image")
            url = self.url
            # print (" URL:" + self.url)
            self.last_parameters = None
            self.retorno = requests.post(url, files={'file': open(caminho_imagem, 'rb')})
            # if self.success():
            #     print ("POST OK: ", self.url, self.last_parameters)
            # print ("Api Post Image Concluido")
            return self.retorno
        except Exception as e:
            raise e

    def put(self):
        try:
            # print ("Api Put")
            url = self.url
            # print (" URL:" + self.url)
            self.last_parameters = self.parameters
            self.retorno = requests.put(url, json=self.parameters)
            # if self.success():
            #     print ("PUT OK: ", self.url, self.last_parameters)
            # print ("Api Put Concluido")
            return self.retorno
        except Exception as e:
            raise e

    def delete(self):
        try:
            url = self.url
            self.last_parameters = {}
            self.retorno = requests.delete(url)
            return self.retorno
        except Exception as e:
            raise e

    def validar_retorno(self, retorno_esperado):
        # print ("Validar Retorno")
        # print ("Retorno esperado:", retorno_esperado)
        # print ("Retorno da API:", self.retorno.status_code)

        json_enviado = json.dumps(self.last_parameters, indent=4, sort_keys=True, separators=(',', ': '))
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201:
            json_recebido = json.dumps(self.retorno.json(), indent=4, sort_keys=True, separators=(',', ': '))
        else:
            json_recebido = self.retorno.text
        assert self.retorno.status_code == retorno_esperado, "O resultado esperado [%d] e diferente do retorno [%d].\n\tURL=%s\n\tParametros enviados=%s\n\tRetorno=%s" % (retorno_esperado, self.retorno.status_code, self.url, json_enviado, json_recebido)

        self._verify_error_response(self.retorno)

    def success(self):
        return  self.retorno.status_code >= 200 and self.retorno.status_code <= 204

    def assert_result(self, field_name, expected_result):
        json_enviado = json.dumps(self.last_parameters, indent=4, sort_keys=True, separators=(',', ': '))
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201:
            json_recebido = json.dumps(self.retorno.json(), indent=4, sort_keys=True, separators=(',', ': '))
        else:
            json_recebido = self.retorno.text
        result = self.retorno.json()[field_name]
        assert result == expected_result, "O resultado esperado [%s] e diferente do retorno [%s].\n\tURL=%s\n\tParametros enviados=%s\n\tRetorno=%s" % (expected_result, result, self.url, json_enviado, json_recebido)

    def json_return_value(self, key):
        msg = 'Chave %s nao encontrada no retorno: %s' % (key, pretty_json(self.retorno.json()))
        assert key in self.retorno.json(), msg
        return self.retorno.json()[key]

    def _verify_error_response(self, api_response):
        """ Verifica a estrutura de retorno em caso de erro. """
        if api_response.status_code < 400 or api_response.status_code > 499:
            return

        # TODO: A Api, caso nao encontre a rota, gerar um 404 default, sem um JSON.
        # TODO: Temos que alterar isso na API loggingo que possivel.

        try:
            error_response = api_response.json()
        except Exception as e:
            if api_response.status_code == 404:
                return
