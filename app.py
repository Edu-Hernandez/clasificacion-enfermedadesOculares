import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

# Ruta donde se guardarán las imágenes subidas
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Extensiones permitidas para los archivos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Cargar el modelo entrenado
model = load_model('models/model.h5')

# Función para verificar si la extensión del archivo es permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para clasificar la imagen subida
@app.route('/classify', methods=['POST'])
def classify():
    if 'img' not in request.files:
        return redirect(request.url)
    
    file = request.files['img']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Cargar y preprocesar la imagen
        img = image.load_img(file_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        
        # Hacer la predicción
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        
        # Mapeo de índices a nombres de enfermedades
        disease_classes = ['Otras enfermedades/anomalías (O)', 'normal (N)', 'Miopía Patológica (M)', 'Hipertensión (H)', 'Glaucoma (G)', 'Diabetes (D)', 'Catarata (C)', 'Degeneración macular relacionada con la edad (A)']
        classification = disease_classes[predicted_class]
        
        return render_template('index.html', img_path=file_path, classification=classification)
    
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
