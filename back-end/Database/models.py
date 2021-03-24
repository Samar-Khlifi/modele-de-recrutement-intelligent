from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash




class Entreprise(db.Document):   # créer un document entreprise
    nom=db.StringField(required=True)
    Fax=db.IntField(required=True)
    email=db.EmailField(required=True,unique=True)
    password=db.StringField(required=True)
    specialite=db.StringField(required=True)
    adresse=db.StringField(required=True)
    tel=db.IntField(required=True)
    added_by=db.ReferenceField('Role')
    offre=db.ListField(db.ReferenceField('offre_emploi'))
    meta = {'strict': False}



    def hash_password(self):
        self.password= generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password,password)



class Candidat(db.Document):   # créer un document candidats
    First_name=db.StringField(required=True)
    Last_name=db.StringField(required=True)
    email=db.EmailField(required=True,unique=True)
    password=db.StringField(required=True)

    tel=db.IntField(required=True)
    adresse=db.StringField(required=True)
    added_by=db.ReferenceField('Role')
    apprentissage=db.ReferenceField('Apprentissage')
    def hash_password(self):
        self.password= generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password,password)
    meta = {'strict': False}




class Role(db.Document):
    name=db.StringField(required=True)
    meta = {'strict': False}



class offre_emploi(db.Document):
    date_debut=db.DateTimeField(format="dd/mm/yyyy")
    date_fin=db.DateTimeField(required=True)
    type_post=db.StringField(required=True)
    type_contrat=db.StringField(required=True)
    description_offre=db.StringField(required=True)
    entreprise=db.ReferenceField('Entreprise')
    cv=db.ReferenceField('photo')




class Photo(db.Document):
    titre_cv=db.StringField(required=True)
    candidat=db.ReferenceField('Candidat')
    meta = {'strict': False}
    




class Apprentissage(db.Document):
    python=db.IntField(required=True)
    C=db.IntField(required=True)
    Raspberry=db.IntField(required=True)
    Js=db.IntField(required=True)
    Linux=db.IntField(required=True)

    candidat=db.ReferenceField('Candidat')
    meta = {'strict': False}



