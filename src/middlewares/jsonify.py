import json
import falcon


class JsonifyMiddleware(object):
    def process_request(self, req, resp):
        req.json = {}

        if not req.content_length:
            return
        body = req.stream.read()

        try:
            req.json = json.loads(body.decode('utf-8'))

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Syntax error')
        except UnicodeDecodeError:
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Invalid encoding',
                                   'Could not decode as UTF-8')


    def process_response(self, req, resp, resource, req_succeeded):
        try:
            resp.data = json.dumps(resp.json)
        except AttributeError:
            pass
