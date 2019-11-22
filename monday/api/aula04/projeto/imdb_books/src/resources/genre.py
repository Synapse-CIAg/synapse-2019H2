import falcon
import json
import datetime
from database import db

class GenreResource():

    def on_get(self, request, resp):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM genres")

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(list(cursor.fetchall()), default=str)

    def on_get_genre(self, request, resp, id):
        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM authors WHERE id = %s", (id,))

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(cursor.fetchone(), default=str)


    def on_post(self, req, resp):
        novoGenero = json.loads(req.stream.read().decode('utf-8'))
        tuplaGenero = (novoGenero['name'],)

        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO genres (name) VALUES (%s)", (tuplaGenero))

        db.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(novoGenero, default=str)

    def on_put(self, req, resp):
        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return
        
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM genres WHERE id = %s", (id,))

        genero = cursor.fetchone()

        if (genero is None):
            erro = {
                'mensagem': 'Nao ha registro de genero para o id informado.'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        generoAlterado = json.loads(req.stream.read().decode('utf-8'))
        tuplaEdicaoDeGenero = (generoAlterado['name'],)

        cursor = db.cursor(dictionary=True)
        cursor.execute("UPDATE genres SET name = %s", (tuplaEdicaoDeGenero))

        db.commit()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(generoAlterado, default=str)

    def on_delete_genre(self, req, resp, id):
        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        cursor = db.cursor(dictionary=True)
        cursor.execute("DELETE FROM genres WHERE id = %s", (id,))

        db.commit()
        resp.status = falcon.HTTP_204