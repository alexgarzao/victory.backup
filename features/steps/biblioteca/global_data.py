# TODO: class Variables?
class GlobalData (object):

    def __init__(self):
        self.variables = {}

    def set_variable_result(self, variable, value):
        # Se necessario remove o $ no inicio do nome da variavel.
        if variable[0] == '$':
            variable = variable[1:]
        self.variables[variable] = value

    def get_variable_result(self, variable):
        try:
            dot_position = variable.find('.')
            if dot_position == -1:
                struct=""
                field = variable
                return self.variables[field]

            struct = variable[:dot_position]
            field = variable[dot_position + 1:]
            return self.variables[struct][field]
        except:
            message = "GlobalData: Erro ao tentar obter o conteudo da variavel.\n"
            message += "GlobalData: Variaveis definidas: %s\n" % self.variables.keys()
            message += "GlobalData: Tentando obter a variavel '%s': struct='%s' field='%s'.\n" % (variable, struct, field)
            assert False, message


    def get_content(self, content):
        if type(content) == str and content and content[0] == '$':
            return self.get_variable_result(content[1:])

        return content
