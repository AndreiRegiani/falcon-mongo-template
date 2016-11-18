import falcon

from decorators import require
from models import ExampleModel


class ExampleResource(object):
    def on_get(self, req, resp):
        rows = []
        for i in ExampleModel.objects:
            row = {
                'email': i.email,
                'name': i.name
            }
            rows.append(row)

        resp.json = rows
        resp.status = falcon.HTTP_200


    @require('email', 'name')
    def on_post(self, req, resp):
        row = ExampleModel(
            email = req.json['email'],
            name = req.json['name']
        )
        row.save()

        resp.json = {'id': str(row.id)}
        resp.status = falcon.HTTP_201
