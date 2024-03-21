from fastapi import FastAPI, File, UploadFile, HTTPException
from package_folder.img_preprocessing import img_preprocessing
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
#from fastapi.responses import JSONResponse

api = FastAPI()

#define a root `/` endpointk
@api.get("/")
def index():
    return {"greeting": "well done"}

'''
@api.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents))
    img = getImage(img)  # Ensure this function adjusts the image to the expected input format
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)  # Use np.expand_dims for clarity
    print(img)
    model = load_model('models/model.h5')
    res = model.predict(img)[0][0]
    if res < 0.5:
        mole = 'Melanoma'
        prob = 1 - res
    else:
        mole = 'NotMelanoma'
        prob = res
    #return JSONResponse(content={"Mole_prediction": mole, "Probability": prob})
    return {"Mole_prediction": mole}
'''

'''
@api.post("/predict")
async def predict(img: UploadFile = File(...)):
    img = img.file.read()
    ######################
    img = Image.open(BytesIO(img))
    print(img.size)

    img_pre_proc=img_preprocessing(img)
    print('success')
    model = load_model('models/base_model_01.keras')
    res = model.predict(img_pre_proc)[0][0]
    res_type=type(res)
    print (f'RESULT IS {res}, with type {res_type}')

    if res < 0.5:
        mole = 'Melanoma'
        prob = str(1 - res)
    else:
        mole = 'NotMelanoma'
        prob = str(res)
    print (f"Mole_prediction: {mole}, with probability of: {prob}")
    return {"Mole_prediction": mole, "with probability of": prob}
    '''

'''
# @api.post("/predict")
# async def predict(img: UploadFile = File(...)):
#     img = img.file.read()
#     img = Image.open(BytesIO(img))
#     img_pre_proc=img_preprocessing(img)
#     model = load_model('models/base_model_01.keras')
#     res = model.predict(img_pre_proc)[0][0]
#     if res < 0.5:
#         mole = 'Melanoma'
#         prob = str(1 - res)
#     else:
#         mole = 'NotMelanoma'
#         prob = str(res)
#     return {"Mole_prediction": mole, "with probability of": prob}'''

@api.post("/predict")
async def predict(img):
    img = img.file.read()
    ######################
    img = Image.open(BytesIO(img))
    print(img.size)

    img_pre_proc=img_preprocessing(img)
    print('success')
    model = load_model('models/base_model_01.keras')
    res = model.predict(img_pre_proc)[0][0]
    res_type=type(res)
    print (f'RESULT IS {res}, with type {res_type}')

    if res < 0.5:
        mole = 'Melanoma'
        prob = str(1 - res)
    else:
        mole = 'NotMelanoma'
        prob = str(res)
    print (f"Mole_prediction: {mole}, with probability of: {prob}")
    return {"Mole_prediction": mole, "with probability of": prob}

'''# @api.post("/predict")
# async def predict(img: UploadFile = File(...)):
#     img_data = img.file.read()
#     img = Image.open(BytesIO(img_data))
#     img_pre_proc = img_preprocessing(img)
#     model = load_model('models/plant_model_weights.keras')
#     res = model.predict(img_pre_proc)[0][0]
#     if res < 0.5:
#         mole = 'Melanoma'
#         prob = str(1 - res)
#     else:
#         mole = 'NotMelanoma'
#         prob = str(res)
#     return {"Mole_prediction": mole, "Probability": prob}  # Ensure prob is converted to float if necessary'''
