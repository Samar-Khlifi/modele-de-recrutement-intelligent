from database.models import offre_emploi
from flask_restful import Resource
from flask import request,Response


class Offre(Resource):

    def post(self):
        
        body=request.get_json()
        offre=offre_emploi(**body)
        offre.save()
        id=offre.id
        return{'id':str(id)},200

    def get(self):
        offre=offre_emploi.objects().to_json()
        return Response(offre,mimetype='application/json',status=200)

class Offres(Resource):
    def get(self,id):
        offres=offre_emploi.objects.get(id=id).to_json()
        return Response(offres,mimetype='application/json',status=200)
    
    def put(seld,id):
        body=request.get_json()
        Offres=offre_emploi.objects().get(id=id).update(date_debut=body['date_debut'],date_fin=body['date_fin'])
        return {"message":"sucessefuly updated"}
    def delete(self,id):
        body=request.get_json()
        Offres=offre_emploi.objects().get(id=id).delete()
        return {"message":"successefuly deleted"}
