import falcon

from models import ExampleModel


class ExampleResource(object):
    def on_get(self, req, resp):
        rows = []
        for i in ExampleModel.objects:
            row = {
                'id': str(i.id),
                'email': i.email
            }
            rows.append(row)

        resp.json = rows
        resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        try:
            email = req.json['email']
        except KeyError, e:
            raise falcon.HTTPBadRequest(
                'Missing JSON Field',
                'Field %s is required' % e
            )

        row = ExampleModel(email=email)
        row.save()

        resp.json = {'id': str(row.id)}
        resp.status = falcon.HTTP_201


    def on_patch(self, req, resp):
        pass


    def on_delete(self, req, resp):
        pass
