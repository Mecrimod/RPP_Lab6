from peewee import Model, IntegerField, CharField, PrimaryKeyField
from database_con import db

class Stan(Model):
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

class inf_stan(Model):
    model=CharField()
    date_buy=CharField()
    number_stan = PrimaryKeyField()
    class Meta:
        database = db
        schema = 'stan'
        table_name = 'stan_infor'
