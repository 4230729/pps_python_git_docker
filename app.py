from flask import Flask, request, jsonify
from bayeta import frotar, añadir_frases

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    frases = frotar()
    return jsonify(frases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
