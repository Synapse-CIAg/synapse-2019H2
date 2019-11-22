import falcon
import json
import datetime
from database import db

class UserResource():

    def on_get(self, request, resp):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(list(cursor.fetchall()), default=str)

    def on_get_user(self, request, resp, id):
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
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(cursor.fetchone(), default=str)


    def on_post(self, req, resp):
        novoUsuario = json.loads(req.stream.read().decode('utf-8'))
        tuplaUsuario = (novoUsuario['user_name'], novoUsuario['fullname'])

        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO users (user_name, fullname) VALUES (%s, %s)", (tuplaUsuario))

        db.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(novoUsuario, default=str)

    def on_put_user(self, req, resp, id):
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
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))

        usuario = cursor.fetchone()

        if (usuario is None):
            erro = {
                'mensagem': 'Nao ha registro de usuario para o id informado.'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        usuarioAlterado = json.loads(req.stream.read().decode('utf-8'))
        tuplaEdicaoDeUsuario = (usuarioAlterado['user_name'], usuarioAlterado['fullname'])

        cursor = db.cursor(dictionary=True)
        cursor.execute("UPDATE users SET user_name = %s, fullname = %s", (tuplaEdicaoDeUsuario))

        db.commit()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(usuarioAlterado, default=str)

    def on_delete_user(self, req, resp, id):
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
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))

        db.commit()
        resp.status = falcon.HTTP_204