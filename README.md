# Flask Translation API (English to Spanish)

This project provides a simple web-based translation service using Flask and the `Helsinki-NLP/opus-mt-en-es` model from the Hugging Face Transformers library. The API allows users to translate English text into Spanish via a web interface or an API endpoint.

## Features
- REST API for English-to-Spanish translation
- Simple web interface for testing translations
- CORS enabled for cross-origin requests

## Requirements
Ensure you have Python 3.8+ installed. You will also need the following dependencies:

### Install Dependencies
Run the following command to install the required Python packages:

```bash
pip install flask flask-cors torch transformers sentencepiece
```

## Running the Application
1. Clone this repository:

```bash
git clone https://github.com/evelyncueva/NLP-Course.git
cd NLP-Course
```

2. Run the Flask application:

```bash
python app.py
```

By default, the server runs on `http://127.0.0.1:5555/`.

## Usage
### Web Interface
Open your browser and go to:

```
http://127.0.0.1:5555/
```

Enter text in English and click "Translate" to get the Spanish translation.

### API Endpoint
You can also send a request to the API endpoint:

#### **Request:**
```bash
curl -X POST "http://127.0.0.1:5555/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, how are you?"}'
```

#### **Response:**
```json
{
  "translated_text": "Hola, ¿cómo estás?"
}
```

## Customization
You can modify the `app.py` file to:
- Use a different translation model.
- Deploy the app on a cloud server (e.g., AWS, Heroku, or Google Cloud).
- Enhance the frontend interface.

## License
This project is open-source and licensed under the MIT License.

## Author
Evelyn Cueva - [GitHub](https://github.com/evelyncueva)

## Acknowledgment
This code is part of the material shared by Juan Pablo Zaldumbide in the NLP Course as part of the AI Master Program at USFQ.
