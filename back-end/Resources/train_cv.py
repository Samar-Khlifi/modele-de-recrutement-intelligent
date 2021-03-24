import numpy as np#opération matricielle
import cv2#traitement d'image
import os#lecture data
from sklearn.model_selection import train_test_split#divsion data en X_train,X_test,y_train,y_test
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator#augmentation taux d'apprentissage
from keras.utils.np_utils import to_categorical#coda binaire output
from keras.models import Sequential#création réseau de neurone
from keras.layers import Dense#nombre classe
from keras.optimizers import Adam#accuracy,loss,val_accuracy,val_loss
from keras.layers import Dropout,Flatten#couche d'applatissement
from keras.layers.convolutional import Conv2D,MaxPooling2D#conv2D:couche de convolution,MzxPooling2D:couche de mise en commun


################ PARAMETERS ########################
path = 'mydata'#emplacement du data
testRatio = 0.2#les données de test sont 20% des données
valRatio = 0.2#les données de validation sont 20% données d'entrainement
imageDimensions= (300,300,3)#resize image 32 32    3 car nous avons image couleur(RGB)
batchSizeVal= 5#l'entrainement se fait sur 5images
epochsVal = 1 #retropropagation


####################################################

#### IMPORTING DATA/IMAGES FROM FOLDERS 
count = 0
images = []     # liste vide dans laquelle on va mettre les nouvelles images(32 32)
classNo = []    # liste vide dans laquelle on va mettre les classes associés aux images 
myList = os.listdir(path)#lecture data sous forme liste
#myList=[0,1,2,3,4]
print("Total Classes Detected:",len(myList))
noOfClasses = len(myList)#nombre des classes qui sont 2
print("Importing Classes .......")
for x in range (0,noOfClasses):
    myPicList = os.listdir(path+"/"+str(x))
    for y in myPicList:
        curImg = cv2.imread(path+"/"+str(x)+"/"+y)#lecture image sous forme matrice
        curImg = cv2.resize(curImg,(300,300))#transformation dimension image sous forme 32 32
        images.append(curImg)
        classNo.append(x)
    print(x,end= " ")
print(" ")
print("Total Images in Images List = ",len(images))
print("Total IDS in classNo List= ",len(classNo))

#### CONVERT TO NUMPY ARRAY 
images = np.array(images)
classNo = np.array(classNo)
print(images.shape)

#### SPLITTING THE DATA
X_train,X_test,y_train,y_test = train_test_split(images,classNo,test_size=testRatio)
X_train,X_validation,y_train,y_validation = train_test_split(X_train,y_train,test_size=valRatio)
print(X_train.shape)
print(X_test.shape)
print(X_validation.shape)



#### PREPOSSESSING FUNCTION FOR IMAGES FOR TRAINING 
def preProcessing(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#transform image couleur au niveau de gris
    img = cv2.equalizeHist(img)#normalisation image
    img = img/255
    return img

# img = preProcessing(X_train[30])
# img = cv2.resize(img,(300,300))
# cv2.imshow("PreProcesssed",img)
# cv2.waitKey(0)

X_train= np.array(list(map(preProcessing,X_train)))
X_test= np.array(list(map(preProcessing,X_test)))
X_validation= np.array(list(map(preProcessing,X_validation)))


#### RESHAPE IMAGES 
X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],X_train.shape[2],1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1)
X_validation = X_validation.reshape(X_validation.shape[0],X_validation.shape[1],X_validation.shape[2],1)

#### IMAGE AUGMENTATION 
dataGen = ImageDataGenerator(width_shift_range=0.1,
                             height_shift_range=0.1,
                             zoom_range=0.2,
                             shear_range=0.1,
                             rotation_range=10)#augmentation de taux d'apprentissage
dataGen.fit(X_train)

#### ONE HOT ENCODING OF MATRICES
y_train = to_categorical(y_train,noOfClasses)
y_test = to_categorical(y_test,noOfClasses)
y_validation = to_categorical(y_validation,noOfClasses)

#### CREATING THE MODEL 
def myModel():
    noOfFilters = 15
    sizeOfFilter1 = (3,3)
    sizeOfFilter2 = (3, 3)
    sizeOfPool = (2,2)
    noOfNodes= 10

    model = Sequential()#création d'un reseau de neurone vide
    model.add((Conv2D(noOfFilters,sizeOfFilter1,input_shape=(imageDimensions[0],
                      imageDimensions[1],1),activation='relu')))
    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu',padding="same")))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu',padding="same")))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu',padding="same")))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu',padding="same")))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(6,activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(noOfClasses, activation='softmax'))

    model.compile(Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

model = myModel()
print(model.summary())

#### STARTING THE TRAINING PROCESS
history = model.fit_generator(dataGen.flow(X_train,y_train,
                                 batch_size=batchSizeVal),
                                 steps_per_epoch=len(X_train) //batchSizeVal ,
                                 epochs=epochsVal,
                                 validation_data=(X_validation,y_validation),
                                 shuffle=1)
                                 

#### PLOT THE RESULTS  
# plt.figure(1)
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.legend(['training','validation'])
# plt.title('Loss')
# plt.xlabel('epoch')
# plt.figure(2)
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.legend(['training','validation'])
# plt.title('Accuracy')
# plt.xlabel('epoch')
# plt.show()
model.save("model_cv1.h5")

