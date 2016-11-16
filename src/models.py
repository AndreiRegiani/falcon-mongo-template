from mongoengine import *


class ExampleModel(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=64)
    last_name = StringField(max_length=64)
