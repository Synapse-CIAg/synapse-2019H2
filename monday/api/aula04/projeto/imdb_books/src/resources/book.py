import falcon
import json
from database import db

class BookResource():

    def on_get(self, request, resp):

        cursor = db.cursor(dictionary=True)

        # cur.execute("SELECT * FROM books WHERE title = %s AND id = %s;", (1))
        cursor.execute("SELECT * FROM books")

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(list(cursor.fetchall()))

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "book - post" })

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "book - put" })

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "book - delete" })