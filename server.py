from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = float(data.get('num1', 0))
    num2 = float(data.get('num2', 0))

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'})
        result = num1 / num2
    elif operation == 'modulo':
        if num2 == 0:
            return jsonify({'error': 'Cannot modulo by zero'})
        result = num1 % num2
    elif operation == 'power':
        result = math.pow(num1, num2)
    elif operation == 'sqrt':
        if num1 < 0:
            return jsonify({'error': 'Cannot sqrt a negative number'})
        result = math.sqrt(num1)
    else:
        return jsonify({'error': 'Unknown operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
