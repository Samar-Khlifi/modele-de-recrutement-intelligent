from database.models import Photo
from flask import request,Response,jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from Resources.errors import SchemaValidationError, ProduitAlreadyExistsError, InternalServerError, UpdatingProduitError, DeletingProduitError, ProduitNotExistsError
from werkzeug.utils import secure_filename
import os
from app import app
import keras

import numpy as np
import numpy as np
import cv2
import pickle
from keras.models import load_model



font = cv2.FONT_HERSHEY_SIMPLEX

import tensorflow as tf
graph = tf.get_default_graph()


session = keras.backend.get_session()
init = tf.global_variables_initializer()
session.run(init)

# tf.errors.FailedPreconditionError(é
#     node_def, op, message
# )


from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model
from keras import backend as k
# tf_config = some_custom_config
# sess = tf.Session(config=tf_config)
# graph = tf.get_default_graph()

# set_session(sess)

session = tf.Session(graph=tf.Graph())
with session.graph.as_default():
    k.backend.set_session(sess)
 
# IMPORT THE TRANNIED MODEL
model=load_model("model_cv1.h5")



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



class upload(Resource):
    def post(self):
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            body = {"titre_cv":filename,"candidat":request.form.get('id')}
            photo=Photo(**body).save()
            
            
            file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            print("gggg",file_path)
            cv2.imread(file_path)
            imgOrignal=cv2.imread(file_path)
            img = cv2.resize(imgOrignal, (300, 300))
            img = preprocessing(img)
            img = img.reshape(1, 300, 300, 1)
            global sess
            global graph
            with graph.as_default():
                set_session(sess)
            with graph.as_default():
                predictions = model.predict(img)
            with session.graph.as_default():
                k.backend.set_session(session)
                model.predict(x, **kwargs)
            print("bbbb",predictions)


            
            #y = model.predict(X) 
            classIndex = model.predict_classes(img)
            probabilityValue =np.amax(predictions)
            if probabilityValue > 0.5:

                print("aaaa",classIndex)
                print("cccc",getCalssName(classIndex))
                window_name='samar'
    
                org = (50, 50) 
    
    # fontScale 
                fontScale = 1
    
    # Blue color in BGR 
                color = (255, 0, 0) 
    
    # Line thickness of 2 px 
                thickness = 2
    
    # Using cv2.putText() method 
                image = cv2.putText(imgOrignal, str(getCalssName(classIndex)), org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 
            cv2.imshow(window_name,image ) 

            resp = jsonify({'message': str(getCalssName(classIndex))})
            resp.statu_code = 201
            return resp
        else:
            resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp



def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img
def getCalssName(classNo):
    if   classNo == 0: return 'class 0'
    elif classNo == 1: return 'class 1'



#imgOrignal=cv2.imread(file_path)
# img = cv2.resize(imgOrignal, (300, 300))
# img = preprocessing(img)

# img = img.reshape(1, 300, 300, 1)

# predictions = model.predict(img)

# print("bbbb",predictions)

# classIndex = model.predict_classes(img)
# probabilityValue =np.amax(predictions)
# if probabilityValue > 0.5:

#     print("aaaa",classIndex)
#     print("cccc",getCalssName(classIndex))
#     window_name='samar'
    
#     org = (50, 50) 
    
#     # fontScale 
#     fontScale = 1
    
#     # Blue color in BGR 
#     color = (255, 0, 0) 
    
#     # Line thickness of 2 px 
#     thickness = 2
    
#     # Using cv2.putText() method 
#     image = cv2.putText(imgOrignal, str(getCalssName(classIndex)), org, font,  
#                     fontScale, color, thickness, cv2.LINE_AA) 
   
# Displaying the image 
    #cv2.imshow(window_name,image ) 
cv2.waitKey(0)
cv2.destroyAllWindows()