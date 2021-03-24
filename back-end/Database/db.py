from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)


#Ici, nous avons importé MongoEngine et créé l' db objet et nous avons défini une fonction initialize_db() que
# nous allons appeler de notre app.py pour initialiser la base de données.