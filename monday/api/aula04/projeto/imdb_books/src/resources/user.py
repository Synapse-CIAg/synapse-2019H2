import falcon
import json

class UserResource():

    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "user - get" })

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "user - post" })

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "user - put" })

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "user - delete" })