from peewee import *
from os import path

ROOT =path.dirname(path.realpath(__file__))
db=SqliteDatabase(path.join(ROOT,"Activities.db"))

class Activities(Model):
    name=CharField()
    desc=CharField()
    location=CharField()

    class Meta:
        database=db

Activities.create_table(fail_silently=True)
Activities.create(name="Graduation",desc="Graduating",location="eMobilis")
Activities.create(name="Running",desc="Competition",location="Kasarani")
Activities.create(name="Crusade",desc="Revival",location="Uhuru Park")


activity1 = Activities.get(id=1)
print(activity1.name,activity1.desc,activity1.location)
activity2 = Activities.get(id=2)
print(activity2.name,activity2.desc,activity2.location)