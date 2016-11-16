import falcon
import mongoengine as mongo

import settings
from middlewares.json import JsonMiddleware


api = falcon.API(middleware=[
    JsonMiddleware(),
])

mongo.connect(
    settings.MONGO['DATABASE'],
    host = settings.MONGO['HOST'],
    port = settings.MONGO['PORT'],
    username = settings.MONGO['USERNAME'],
    password = settings.MONGO['PASSWORD']
)
