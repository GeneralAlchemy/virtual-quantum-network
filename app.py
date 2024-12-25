from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Quantum Network API is running!"

@app.route("/apply-gate", methods=["POST"])
def apply_gate():
    data = request.json
    gate = data.get("gate")
    # Example response (logic can be expanded)
    return jsonify({"status": "success", "applied_gate": gate})

if __name__ == "__main__":
    app.run(debug=True)
