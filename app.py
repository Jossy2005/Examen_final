from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "La API funciona"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Debe enviar el campo 'text'"}), 400
    text = data["text"]
    respuesta = f"IA procesó tu texto: {text}"
    return jsonify({"result": respuesta}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
