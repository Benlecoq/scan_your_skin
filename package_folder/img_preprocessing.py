from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

def get_image(img):
    img = img.resize((224, 224))
    return img

def img_preprocessing(img):
    #img = Image.open(img)
    img = get_image(img)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img
