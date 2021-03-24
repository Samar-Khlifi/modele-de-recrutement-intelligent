from database.models import Entreprise
from flask_restful import Resource
from flask import request,make_response,jsonify
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from Resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError


class Signup(Resource): 
    #Resource: classe de base qui peut définir le routage pour une ou plusieurs méthodes HTTP pour une URL donnée.
    
    def post(self):
        try:
            body = request.get_json()
            entreprise = Entreprise(**body)
            entreprise.hash_password()
            entreprise.save()
            id = entreprise.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError
        
        

     
       



class Login(Resource):
    def post(self):
        try:
            body = request.get_json()
            entreprise = Entreprise.objects.get(email=body.get('email'))
            authorized = entreprise.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            #expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=str(entreprise.id))
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': access_token,
                'entreprise': entreprise
            }
            return make_response(jsonify(responseObject), 200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError



        


