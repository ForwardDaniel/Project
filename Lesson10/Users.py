from peewee import *
from os import path

ROOT =path.dirname(path.realpath(__file__))
db=SqliteDatabase(path.join(ROOT,"persons.db"))

class Person(Model):
    name = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    password = CharField
    class Meta:
        database = db

Person.create_table(fail_silently=True)
Person.create(name = "Dan",email = "dan@gmail.com",age = "18",password = "dan123")
Person.create(name = "Brio",email = "brio@gmail.com",age = "28",password = "brio123")