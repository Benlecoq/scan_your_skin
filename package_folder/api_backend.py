from fastapi import FastAPI, File, UploadFile
#import tensorflow as tf
from package_folder.img_preprocessing import getImage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from io import BytesIO
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import requests


api = FastAPI()

# define a root `/` endpoint
@api.get("/")
def index():
    return {"greeting": "well done"}

'''
@api.get("/predict")
def predict(feature1, feature2):

    #model = tf.keras.saving.load_model("the path to the model folder")
    #prediction = model.predict(inputs needed)
    #pretty_prediction = from_number_to_string(float(prediction[0]))

    # Here, I'm only returning the features, since I don't actually have a model.
    # In a real life setting, you would return the predictions.
    #return {'prediction': pretty_prediction}
    return {'prediction': int(feature1)*int(feature2)}'''
'''
@api.get("/predict")
def predict(image_path):
    response = requests.get(image_path)
    img = Image.open(BytesIO(response.content))

    img = getImage(img)
    img = img_to_array(img)
    img = img.reshape((-1, 224, 224, 3))
    model = load_model('models/model.h5')
    res = model.predict(img)[0][0]
    if(res < 0.5):
      mole = 'Melanoma' #how do we know that 0 is melanoma?
      prob = 1-res
    if(res >= 0.5):
      mole = 'NotMelanoma'   #how do we know that 1 is not melanoma?
      prob = res
      print('Mole : ', mole)
      print('Probability = ', prob)

      return {'Mole_prediction': mole} '''


@api.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents))
    img = getImage(img)  # Ensure this function adjusts the image to the expected input format
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)  # Use np.expand_dims for clarity
    model = load_model('models/model.h5')
    res = model.predict(img)[0][0]
    if res < 0.5:
        mole = 'Melanoma'
        prob = 1 - res
    else:
        mole = 'NotMelanoma'
        prob = res
    return JSONResponse(content={"Mole_prediction": mole, "Probability": prob})
