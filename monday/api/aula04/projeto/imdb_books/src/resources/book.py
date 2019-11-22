import falcon
import json
from database import db

class BookResource():

    def on_get(self, request, resp):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(list(cursor.fetchall()))

    def on_get_book(self, request, resp, id):
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
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(cursor.fetchone(), default=str)

    def on_post(self, req, resp):
        novoLivro = json.loads(req.stream.read().decode('utf-8'))

        # realizar verificação do author_id
        # realizar verificação do genre_id
        # realizar verificação se o author_id recebido existe no banco de dados
        # realizar verificação se o genre_id recebido existe no banco de dados

        tuplaLivro = (novoLivro['title'], novoLivro['sinopsis'], novoLivro['release_date'], novoLivro['thumbnail_url'], novoLivro['author_id'])
        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO books (title, sinopsis, release_date, thumbnail_url, author_id) VALUES (%s, %s, %s, %s, %s)", (tuplaLivro))

        bookId = cursor.lastrowid

        tuplaLivroGenero = (bookId, novoLivro['genre_id'])
        cursor.execute("INSERT INTO books_genres (book_id, genre_id) VALUES (%s, %s)", tuplaLivroGenero)

        db.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(novoLivro, default=str)

    def on_put_book(self, req, resp, id):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "book - put" })

    def on_delete(self, req, resp, id):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "book - delete" })