from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from threading import Thread

# Crear la app de Flask
app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)  # Esto habilita CORS para todos los ori­genes


model_name = 'Helsinki-NLP/opus-mt-en-es'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# HTML como un string (lo puedes modificar)
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba de Servicio de Prediccion</title>
    <script>
        async function sendPrediction() {
            const text = document.getElementById("inputText").value;
            const response = await fetch("http://localhost:5555/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();
            document.getElementById("predictionResult").innerText = `Translation: ${data.translated_text}`;
        }
    </script>
</head>
<body>
    <div style="max-width: 600px; margin: 0 auto; text-align: center;">
        <h1>Servicio de Traducción de inglés a español </h1>
        <textarea id="inputText" rows="4" cols="50" placeholder="Write the text to be translated..."></textarea>
        <br><br>
        <button onclick="sendPrediction()">Translate</button>
        <p id="predictionResult" style="margin-top: 20px; font-size: 18px; font-weight: bold;"></p>
    </div>
</body>
</html>
"""

# Ruta para servir el HTML
@app.route("/")
def home():
    return html_content

# Ruta para la prediccion
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_text = data["text"]
    
    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)

    # Generate translation
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
    
    # Decode output tokens
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return jsonify({"translated_text": translated_text})

# Ejecutar Flask en un hilo
def run_flask():
    app.run(host="0.0.0.0", port=5555)

# Crear un hilo para ejecutar Flask
thread = Thread(target=run_flask)
thread.start()