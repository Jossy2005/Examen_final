from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generar_respuesta(pregunta: str) -> str:
    if not pregunta or pregunta.strip() == "":
        return "Escribe una pregunta."
    # Respuesta IA muy simple (simulada)
    if "?" in pregunta:
        return "Respuesta (simulada): depende del contexto, por favor describe más detalles."
    words = pregunta.strip().split()
    if len(words) <= 8:
        return "Respuesta (simulada): " + " ".join(reversed(words))
    return "Resumen (simulado): " + " ".join(words[:12]) + "..."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ia", methods=["POST"])
def ia():
    pregunta = request.form.get("pregunta") or request.json.get("pregunta") if request.is_json else None
    respuesta = generar_respuesta(pregunta)
    return jsonify({"pregunta": pregunta, "respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
