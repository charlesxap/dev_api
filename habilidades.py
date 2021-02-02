from flask_restful import Resource

lista_habilidades = ['Pyhton','Java','Flask','PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades