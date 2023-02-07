from flask import Flask
from flask import request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


# provide a route to the URL
@app.route("/operation", methods=["POST"])
def math_operation():
    if request.method == "POST":
        operation = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        else:
            result = num1 - num2

        return render_template("result.html", result=result)

        # return ("the operation is {} and the result is {}".format(operation, result))


"""@app.route("/demo", methods=["POST"])
def math_operation():
    if request.method == "POST":
        operation = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        else:
            result = num1 - num2

        return ("the operation is {} and the result is {}".format(operation, result)"""


# provide a route to the URL
@app.route("/addition", methods=["POST"])
def math_operation1():
    if request.method == "POST":
        operation = request.json["operation"]
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        result = num1 + num2
        return jsonify("the operation is {} and the result is {}".format(operation, result))


if __name__ == "__main__":
    # local ip adress it will map to it by default host flask runs at 5000/ 5001/8000 port
    app.run(host="0.0.0.0", port=5001)
