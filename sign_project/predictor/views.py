from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
import os
from tensorflow.keras.preprocessing import image as keras_image

model = tf.keras.models.load_model(os.path.join('predictor', 'sign_language_model.h5'))
labels = [ "A", "B", "Blank", "C", "D", "E", "F", "G", "H", "I", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y"]

def index(request):
    prediction = None
    file_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        image = Image.open(fs.path(filename)) # Open the image file
        image = image.convert('RGB')  # Ensure 3 channels
        image = image.resize((128, 128))
        img_array = keras_image.img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 128, 128, 3)
        img_array = img_array / 255.0  # Normalize the image

        prediction_arr = model.predict(img_array)
        predicted_class = np.argmax(prediction_arr)
        prediction = labels[predicted_class]

    return render(request, 'predictor/index.html', {
        'prediction': prediction,
        'file_url': file_url
    })


