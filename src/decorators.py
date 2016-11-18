import falcon


def require(*fields):
    def request(req, resp, resource, params):
        for field in fields:
            if not field in req.json:
                raise falcon.HTTPError(falcon.HTTP_400,
                                       'Missing JSON field',
                                       "Field '%s' is required" % field)
    return falcon.before(request)
