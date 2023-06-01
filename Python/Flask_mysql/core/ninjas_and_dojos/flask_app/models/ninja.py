from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DB
class Ninja:
     def __init__(self,data):
          self.id=data['id']
          self.first_name = data['first_name']
          self.last_name = data['last_name']
          self.age = data['age']
          self.created_at = data['created_at']
          self.updated_at = data['updated_at']
          self.dojo_id=data['dojo_id']

@classmethod
def create_ninja(cls,data):

     query="""INSERT INTO ninjas(first_name,last_name,age,dojo_id)
          VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"""
     print("data est========",data)
     return MySQLConnection(DB).query_db(query,data)

@classmethod
def get_all_ninja(cls):

     query="SELECT * FROM ninjas; "

     results=MySQLConnection(DB).query_db(query)
     table_ninjas=[]
     for row in results :
          table_ninjas.append(cls(row))
          return table_ninjas

@classmethod
def show_ninja_in_dojo(cls,data):
     query="""
     SELECT first_name,last_name,age,dojos.name FROM ninjas
     JOIN dojos on dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s 
          """
     results=MySQLConnection(DB).query_db(query,data)
     ninjas=[]
     if results:

          for row in results :
               data={
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'name':row['name']                
                    }

               ninjas.append(row)



     return ninjas