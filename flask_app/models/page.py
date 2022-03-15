from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User
from flask import flash

class Page:
    db = ("cosmicSite")
    def __init__(self, data):
        self.id = data['id']
        self.header = data['header']
        self.message = data['message']
        self.posted_by = data['posted_by']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        

    @classmethod
    def get_posts(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL(User.db).query_db(query)
        posts = []
        for a in results:
            posts.append(cls(a))
        return posts

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts(header,message) VALUES (%(header)s,%(message)s);"
        result = connectToMySQL(User.db).query_db(query, data)
        return result

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE posts SET header =%(header)s, message= %(message)s, posted_by= %(posted_by)s, updated_on = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)