from peewee import Model, IntegerField, CharField, PrimaryKeyField
from database_con import db

class User(Model):
    num_pokazaina = PrimaryKeyField()
    Date_and_time=CharField()
    Chastota=IntegerField()
    Power=IntegerField()
    temp=IntegerField()
    number_stan=IntegerField()
    class Meta:
        database = db
        schema = 'stan'
        table_name = 'Osn_stan'
