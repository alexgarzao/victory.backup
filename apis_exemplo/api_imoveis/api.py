from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import fields

app = Flask(__name__)
api = Api(app)

# TODO: mover para o feature
IMOVEIS = {}
# IMOVEIS = {
#     '1': {
#         'proprietario': 'Alex',
#         'caracteristicas': ['churrasqueira', 'lareira', 'copa'],
#         'endereco': 'Av das Hortências, 123 - Canoas - RS',
#         'valor': 650000,
#         'esta_ocupado': True,
#     },
#     '2': {
#         'proprietario': 'Yuri',
#         'caracteristicas': ['churrasqueira', 'duplex', 'ar condicionado'],
#         'endereco': 'Rua do Ipiranga, 1009 - Cachoeirinha - RS',
#         'valor': 850000,
#         'esta_ocupado': False,
#     },
#     '3': {
#         'proprietario': 'Wendell',
#         'caracteristicas': ['porcelanato', 'laminado'],
#         'endereco': 'Av Belvedere, 450 - AP 209 - Porto Alegre - RS',
#         'valor': 750000,
#         'esta_ocupado': True,
#     },
# }


def abort_if_imovel_doesnt_exist(imovel_id):
    if imovel_id not in IMOVEIS:
        abort(404, message="Imovel {} nao existe".format(imovel_id))

imovel_parser = reqparse.RequestParser()
imovel_parser.add_argument('proprietario', required=True, type=str)
imovel_parser.add_argument('caracteristicas', required=True, type=str, action='append')
imovel_parser.add_argument('endereco', required=True)
imovel_parser.add_argument('valor', required=True)
imovel_parser.add_argument('esta_ocupado', required=True, type=bool)

login_parser = reqparse.RequestParser()
login_parser.add_argument('usuario', required=True, type=str)
login_parser.add_argument('senha', required=True, type=str)


# BDD
class Bdd(Resource):
    def post(self):
        IMOVEIS.clear()
        return 200

# Login
class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        usuario = args['usuario']
        senha = args['senha']
        if usuario and senha == "senha " + usuario:
            return 204

        abort(404, message="Usuario/senha nao encontrados")

# Imovel
class Imovel(Resource):
    def get(self, imovel_id):
        abort_if_imovel_doesnt_exist(imovel_id)
        return IMOVEIS[imovel_id]

    def delete(self, imovel_id):
        abort_if_imovel_doesnt_exist(imovel_id)
        del IMOVEIS[imovel_id]
        return '', 204

    def put(self, imovel_id):
        args = imovel_parser.parse_args()
        imovel = {'imovel': args['imovel']}
        IMOVEIS[imovel_id] = imovel
        return imovel, 201


# ImovelList
class ImovelList(Resource):
    def get(self):
        imoveis = [IMOVEIS[k] for k in IMOVEIS]
        return imoveis

    def post(self):
        args = imovel_parser.parse_args()
        if args['caracteristicas'] == [None]:
            args['caracteristicas'] = None
        imovel_id = len(IMOVEIS) + 1
        imovel_id = str(imovel_id)
        IMOVEIS[imovel_id] = {
            'proprietario': args['proprietario'],
            'caracteristicas': args['caracteristicas'],
            'endereco': args['endereco'],
            'valor': args['valor'],
            'esta_ocupado': args['esta_ocupado'],
        }

        return IMOVEIS[imovel_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(Bdd, '/bdd-init')
api.add_resource(Login, '/login')
api.add_resource(ImovelList, '/imoveis')
api.add_resource(Imovel, '/imoveis/<imovel_id>')


if __name__ == '__main__':
    app.run(debug=True)
