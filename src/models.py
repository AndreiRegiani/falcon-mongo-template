from mongoengine import *


class ExampleModel(Document):
    email = StringField(required=True, max_length=64)
    name = StringField(required=True, max_length=64)
