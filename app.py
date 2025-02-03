from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n):
    # Return a specific fun fact about Armstrong numbers
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        powers = " + ".join([f"{d}^{len(digits)}" for d in digits])
        return f"{n} is an Armstrong number because {powers} = {n}"
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get('number')

    # Validate input
    if not num or not num.isdigit():
        return jsonify({"number": num, "error": True}), 400

    num = int(num)
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 else "even")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": False,  # Not required, but could be implemented
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

