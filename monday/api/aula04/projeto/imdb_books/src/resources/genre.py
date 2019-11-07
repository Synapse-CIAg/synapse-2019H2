import falcon
import json

class GenreResource():

    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "genre - get" })

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "genre - post" })

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "genre - put" })

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "genre - delete" })