from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np



def predict_image(image, model, class_names):
    # Crear el array con la forma correcta para alimentar el modelo de Keras
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Abrir la imagen y realizar el preprocesamiento
    image = Image.open(image)
    image = image.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Realizar la predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    if confidence_score < 0.70:
        return "No reconocido", confidence_score
    else:
        return class_name[2:], confidence_score
    