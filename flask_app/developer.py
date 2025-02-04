from flask import render_template,redirect,session,request, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.developer import Developer
from flask_app.models.skill import Skill
from flask_app.models.skill_of_developer import Skill_of_developer
#from flask_app.models.count import Count
from flask_app import app


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
    
@classmethod
def get_developer_available(cls):
        query = """select d.name, d.short_bio,d.github_user, d.s.name from developers d LEFT JOIN skill_of_developers sd ON  d.id = sd.developer_id
        LEFT JOIN skills s ON sc.skill_id = s.id 
        where d.available = 1;"""
        results = connectToMySQL('cls.db_name').query_db(query) # Conexión a la base de datos
        users = []
        for row in results:
            users.append(cls, row)
        return users
    
    