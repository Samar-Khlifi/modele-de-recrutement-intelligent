import numpy as np
import numpy as np
import cv2

from matplotlib import pyplot as plt
from keras.models import load_model

#############################################
         # PROBABLITY THRESHOLD

##############################################

# SETUP THE VIDEO CAMERA
font = cv2.FONT_HERSHEY_SIMPLEX


# IMPORT THE TRANNIED MODEL
model=load_model("model_cv1.h5")

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
imgOrignal=cv2.imread(r'C:\Users\Samar_khlifi\Desktop\projet_cv\back_end\c1.PNG')
img = cv2.resize(imgOrignal, (300, 300))
img = preprocessing(img)

img = img.reshape(1, 300, 300, 1)

    # PREDICT IMAGE
predictions = model.predict(img)

print("bbbb",predictions)
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
   
# Displaying the image 
    cv2.imshow(window_name,image ) 
cv2.waitKey(0)
cv2.destroyAllWindows()

