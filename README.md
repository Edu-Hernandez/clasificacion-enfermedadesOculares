# Aplicación Web para Clasificación de Imágenes de Enfermedades Oculares

## Descripción del Proyecto
Esta es una aplicación web desarrollada con Flask que utiliza un modelo preentrenado Inception-v3 para clasificar enfermedades oculares a partir de imágenes subidas. La aplicación permite a los usuarios cargar imágenes (en formatos PNG, JPG, JPEG o GIF) y devuelve un resultado de clasificación que indica si la imagen corresponde a una de las siguientes categorías:  
- Normal (N)  
- Miopía (M)  
- Hipertensión (H)  
- Glaucoma (G)  
- Diabetes (D)  
- Catarata (C)  
- Degeneración Macular Relacionada con la Edad (A)  
- Otras enfermedades/anomalías (O)  

**Autores**: Yannick F. & Alan H.  
**Palabras clave**: Python, Clasificación, Inception-v3, UCV, Aprendizaje Automático, Detección de Enfermedades Oculares

## Características
- Subida de imágenes a través de una interfaz web amigable.
- Clasificación de enfermedades oculares usando un modelo preentrenado Inception-v3.
- Visualización del resultado de la clasificación junto con la imagen cargada.
- Diseño responsivo con Bootstrap para compatibilidad con diversos dispositivos.
- Notificaciones tipo toast para guiar a los usuarios sobre cómo usar la aplicación.

## Tecnologías Utilizadas
- **Backend**: Flask, TensorFlow, Keras, NumPy
- **Frontend**: HTML, Bootstrap 5.3.3, JavaScript, Vue.js (opcional)
- **Modelo**: Modelo preentrenado Inception-v3 (`model.h5`)

## Estructura del Proyecto
```
project_root/
│
├── app.py                    # Aplicación principal de Flask
├── requirements.txt          # Dependencias de Python
├── models/
│   └── model.h5             # Modelo preentrenado Inception-v3
├── static/
│   ├── uploads/             # Directorio para imágenes subidas
│   │   └── thumbnail.svg    # Imagen de marcador de posición
│   └── icon.ico             # Favicon de la aplicación web
├── templates/
│   └── index.html           # Plantilla HTML principal
└── README.md                # Documentación del proyecto
```

## Requisitos Previos
- Python 3.8 o superior
- Entorno virtual (recomendado)
- Archivo del modelo preentrenado (`model.h5`) en el directorio `models/`
- Formatos de imagen soportados: PNG, JPG, JPEG, GIF

## Instalación
1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd <directorio-del-proyecto>
   ```

2. **Configurar un entorno virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Agregar el modelo preentrenado**:
   - Coloca el archivo `model.h5` en el directorio `models/`. Asegúrate de que el directorio exista:
     ```bash
     mkdir models
     ```
   - Si no tienes el modelo, contacta a los autores del proyecto o reentrena el modelo Inception-v3.

5. **Crear el directorio de subidas**:
   ```bash
   mkdir -p static/uploads
   ```
   - Opcionalmente, agrega una imagen de marcador de posición (`thumbnail.svg`) en `static/uploads/`.

6. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```
   La aplicación se iniciará en modo debug y estará disponible en `http://127.0.0.1:5000`.

## Uso
1. **Acceder a la interfaz web**:
   Abre un navegador y navega a `http://127.0.0.1:5000`.

2. **Subir una imagen**:
   - Haz clic en el botón "Subir Imágenes" para seleccionar una imagen (PNG, JPG, JPEG o GIF).
   - La imagen se mostrará en la interfaz.

3. **Clasificar la imagen**:
   - Haz clic en el botón "Clasificar" para procesar la imagen.
   - El resultado de la clasificación (por ejemplo, "Normal (N)", "Glaucoma (G)") aparecerá en el campo de texto.

4. **Limpiar resultados**:
   - Haz clic en el botón "Limpiar Resultados" para restablecer la imagen y la clasificación.

5. **Cómo usar**:
   - Haz clic en el botón "¿Cómo usar?" para mostrar una notificación con instrucciones:
     1. Subir una imagen.
     2. Presionar el botón "Clasificar".
     3. Esperar el resultado.

## Notas
- Asegúrate de que el directorio `models/` contenga el archivo `model.h5` antes de ejecutar la aplicación.
- La aplicación se ejecuta en modo debug por defecto (`app.run(debug=True)`). Para producción, considera usar un servidor WSGI como Gunicorn.
- El directorio `env/` (entorno virtual) debe agregarse a `.gitignore` para evitar incluirlo en el repositorio.
- Si encuentras problemas con las dependencias, asegúrate de que tu versión de Python sea compatible (se recomienda 3.8+).
- La imagen de marcador de posición (`thumbnail.svg`) es opcional, pero mejora la experiencia del usuario.

## Solución de Problemas
- **Modelo no encontrado**: Verifica que `model.h5` esté en el directorio `models/`.
- **Fallo al subir imágenes**: Asegúrate de que el directorio `static/uploads/` exista y tenga permisos de escritura.
- **Errores de dependencias**: Ejecuta `pip install -r requirements.txt` en un entorno virtual limpio.
- **Conflicto de puerto**: Si el puerto 5000 está en uso, cambia el puerto en `app.py` (por ejemplo, `app.run(debug=True, port=5001)`).
