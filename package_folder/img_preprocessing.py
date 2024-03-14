from PIL import Image
import requests
from io import BytesIO

def getImage(img):

  # Grabs an image based on its URL, and resize it

  #response = requests.get(url)
  #img = Image.open(BytesIO(response.content))  # do I need this one?
  #plt.imshow(img)
  img = img.resize((224, 224))
  return img
