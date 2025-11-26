from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------
# Endpoint de prueba (home)
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    """
    Endpoint principal de la API.
    Retorna un mensaje de estado.
    """
    return jsonify({"message": "La API funciona"}), 200


# ------------------------------
# Endpoint predict (IA mínima)
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    """
    Recibe un JSON con {"text": "..."} y devuelve un resultado procesado.
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Debe enviar el campo 'text'"}), 400

    text = data["text"]
    respuesta = f"IA procesó tu texto: {text}"

    return jsonify({"result": respuesta}), 200


# ------------------------------
# Run local
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
