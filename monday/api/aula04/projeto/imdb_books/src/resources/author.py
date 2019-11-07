import falcon
import json

class AuthorResource():

    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "author - get" })

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "author - post" })

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "author - put" })

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "author - delete" })