import json


def jsonify(**kwargs):
    return json.dumps(dict(kwargs))
