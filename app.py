from flask import Flask, render_template, request, jsonify
import operations

app = Flask(__name__)

OPERATIONS = {
    "add": ("Sumar", operations.add, "+"),
    "subtract": ("Restar", operations.subtract, "-"),
    "multiply": ("Multiplicar", operations.multiply, "×"),
    "divide": ("Dividir", operations.divide, "÷"),
    "power": ("Potencia", operations.power, "^"),
    "modulus": ("Módulo", operations.modulus, "%"),
}

@app.route("/")
def index():
    return render_template("index.html", operations=OPERATIONS)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    op_key = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if op_key not in OPERATIONS:
        return jsonify({"error": "Operación inválida"}), 400

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return jsonify({"error": "Números inválidos"}), 400

    name, func, symbol = OPERATIONS[op_key]
    try:
        result = func(a, b)
        return jsonify({"result": result, "operation": f"{a} {symbol} {b} = {result}"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)