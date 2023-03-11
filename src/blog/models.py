import datetime

from mongoengine import (DateTimeField, Document, EmbeddedDocument,
                         EmbeddedDocumentField, ListField, StringField)


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)


class Entry(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.datetime.now())
    headline = StringField(max_length=255)
