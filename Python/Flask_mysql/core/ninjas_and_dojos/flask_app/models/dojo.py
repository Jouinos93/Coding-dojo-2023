from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DB
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_dojo(cls,data):

        query=""" insert into dojos (name)
                value(%(name)s);"""
        result=MySQLConnection(DB).query_db(query,data)
        return (result)


    @classmethod
    def show_dojos(cls):

        query="SELECT * FROM dojos;"
        results_dojo=MySQLConnection(DB).query_db(query)
        table_dojo=[]
        for row in results_dojo :
            table_dojo.append(cls(row))
        return table_dojo
