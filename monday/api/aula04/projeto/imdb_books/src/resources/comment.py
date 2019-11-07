import falcon
import json

class CommentResource():

    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "comment - get" })

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "comment - post" })

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "comment - put" })

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ "method" : "comment - delete" })