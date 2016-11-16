import falcon

from helper import jsonify
from models import ExampleModel


class ExampleResource(object):

    def on_get(self, req, resp):
        rows = []
        for i in ExampleModel.objects:
            row = dict(
                id = str(i.id),
                email = i.email
            )
            rows.append(row)

        resp.data = jsonify(examples=rows)
        resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        row = ExampleModel()
        row.email = 'test@test.com'
        row.first_name = 'Andrei'
        row.last_name = 'Regiani'
        row.save()

        resp.data = jsonify(id=str(row.id))
        resp.status = falcon.HTTP_201


    def on_patch(self, req, resp):
        pass


    def on_delete(self, req, resp):
        pass
