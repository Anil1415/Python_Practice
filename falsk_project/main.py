from flask import Flask
from flask import request

app = Flask(__name__)


# provide a route to the URL
@app.route("/demo", methods=["POST"])
def math_operation():
    if request.method == "POST":
        operation = request.json["operation"]
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        else:
            result = num1 - num2

        return "the operation is {} and the result is {}".format(operation, result)


# provide a route to the URL
@app.route("/addition", methods=["POST"])
def math_operation1():
    if request.method == "POST":
        operation = request.json["operation"]
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        result = num1 + num2
        return "the operation is {} and the result is {}".format(operation, result)


@app.route("/aboutus")
def welcome():
    return "Welcome"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
