from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Queries
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = 
# Validation
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['first_name'])<2:
            is_valid=False
        if len(data['last_name'])<2:
            is_valid=False
        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
        if len(data['password'])<6:
            is_valid=False
        elif data['password'] != data['confirm_password']:
            is_valid=False
        return is_valid
