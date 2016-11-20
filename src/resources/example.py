import falcon

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


    def on_post(self, req, resp):
        email = req.get_json('email', dtype=str, min=6, max=32, default="test@test.com")
        name = req.get_json('name', dtype=str, min=1, max=16, default="Andrei Regiani")

        row = ExampleModel(
            email = email,
            name = name
        )
        row.save()

        resp.json = {'id': str(row.id)}
        resp.status = falcon.HTTP_201
