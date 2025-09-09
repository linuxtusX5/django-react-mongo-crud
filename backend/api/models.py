import mongoengine as me
from django.contrib.auth.hashers import make_password, check_password

class User(me.Document):
    username = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    
class Item(me.Document):
    name = me.StringField(required=True)
    description = me.StringField(required=True)
    created_at = me.DateTimeField(required=True)

    def __str__(self):
        return self.name