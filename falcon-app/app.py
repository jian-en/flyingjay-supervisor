import json
import falcon

class JSONResource(object):
    def on_get(self, request, response):
        response.body = json.dumps({'message': 'Hello, world!'})

app = falcon.API()

app.add_route("/json", JSONResource())
