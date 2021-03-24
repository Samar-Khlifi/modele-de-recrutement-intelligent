from database.models import Role
from flask_restful import Resource
from flask import request
from flask import Response
from flask_jwt_extended import jwt_required, get_jwt_identity



class RoleApi(Resource):

    def post(self):

        body=request.get_json()
        role=Role(**body).save()
        
        id=role.id
        return {'id':str(id)},200

    def get(self):

        role=Role.objects().to_json()
        return Response(role,mimetype="application/json",status=200)


class RolesApi(Resource):

    def get(self,id):

        roles=Role.objects.get(id=id).to_json()
        return Response(roles,mimetype='application/json',status=200)

    def put(self,id):
        body=request.get_json()
        Role.objects.get(id=id).update(name=body['name'])

    def delete(self,id):
        body=request.get_json()
        roles=Role.objects.get(id=id).delete()
        return {'message':'succefuly deleted'},200



