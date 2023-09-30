from mongoengine import Document, StringField, EmailField

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True)

    def __str__(self):
        return self.username
