from app import api
from resources.example import ExampleResource


api.add_route('/api/example', ExampleResource())
