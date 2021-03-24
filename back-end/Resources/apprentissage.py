from database.models import Apprentissage
from flask import Response,request
from flask_restful import Resource
import pickle
import numpy as np


model=pickle.load(open(r"C:\Users\Samar_khlifi\Desktop\IA\save.pkl","rb"))
class apprentissages(Resource):
    def post(self):
        body=request.get_json()
       # print("aaaa",body)
        apprentissage1=Apprentissage(**body)
        #q=np.array([[40,5,2,3,6]])
        #print("cccc",model.predict(q))
        features=[]
        for i in body.values():     # pour n'est pas à chaque fois nda5el matrice de prediction statiquement donc il prend les valus du dictionnaire body qui nous entrons au postman
            features.append(i)
        
        c=[np.array(features)]# double croché car matrice non pas liste
        predict=model.predict(c)
        return {"output":str(predict)}


