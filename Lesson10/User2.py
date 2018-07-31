from peewee import *
from os import path

ROOT =path.dirname(path.realpath(__file__))
db=SqliteDatabase(path.join(ROOT,"persons1.db"))

class Person(Model):
    name = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    password = CharField()
    class Meta:
        database = db

Person.create_table(fail_silently=True)
Person.create(name = input(),email = input(),age = input(),password = input())
Person.create(name = input(),email = input(),age = "28",password = "youw123")
user1 = Person.get(id=1)
print(user1.name,user1.email,user1.password)