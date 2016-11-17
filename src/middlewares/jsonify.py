import json
import falcon


class JsonifyMiddleware(object):
    def jsonify(self, arg, **kwargs):
        if arg:
            return json.dumps(arg)
        return json.dumps(dict(kwargs))

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        try:
            req.json = json.loads(body.decode('utf-8'))

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The JSON was incorrect')
        except UnicodeDecodeError:
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Encoding error',
                                   'Only UTF-8 is supported.')

    def process_response(self, req, resp, resource, req_succeeded):
        try:
            resp.data = self.jsonify(resp.json)
        except AttributeError:
            pass
