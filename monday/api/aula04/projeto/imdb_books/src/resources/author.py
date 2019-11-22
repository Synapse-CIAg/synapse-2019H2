import falcon
import json
import datetime
from database import db

class AuthorResource():

    def on_get(self, request, resp):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM authors")

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(list(cursor.fetchall()), default=str)

    def on_get_author(self, request, resp, id):
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
        novoAutor = json.loads(req.stream.read().decode('utf-8'))
        tuplaAutor = (novoAutor['name'], novoAutor['birth_date'], novoAutor['thumbnail_url'])

        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO authors (name, birth_date, thumbnail_url) VALUES (%s, %s, %s)", (tuplaAutor))

        db.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(novoAutor, default=str)

    def on_put_author(self, req, resp, id):
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

        autor = cursor.fetchone()

        if (autor is None):
            erro = {
                'mensagem': 'Nao ha registro de autor para o id informado.'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        autorAlterado = json.loads(req.stream.read().decode('utf-8'))
        tuplaEdicaoDeAutor = (autorAlterado['name'], autorAlterado['birth_date'], autorAlterado['thumbnail_url'], autor['id'])

        cursor = db.cursor(dictionary=True)
        cursor.execute("UPDATE authors SET name = %s, birth_date = %s, thumbnail_url = %s WHERE id = %s", (tuplaEdicaoDeAutor))

        db.commit()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(autorAlterado, default=str)

    def on_delete_author(self, req, resp, id):
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
        cursor.execute("DELETE FROM authors WHERE id = %s", (id,))

        db.commit()
        resp.status = falcon.HTTP_204
