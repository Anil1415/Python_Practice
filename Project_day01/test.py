from flask import Flask, request, jsonify

app = Flask(__name__)


# decorators

# @app.route('/xyz', methods = ['GET', 'POST'])
@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/xyz', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/anil', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        a = request.json['num5']
        b = request.json['num6']
        result = a * b
        return jsonify(str(result))


if __name__ == '__main__':
    app.run()

"""write a function to fetch data from sql table via API
 and fetch data from mongodb table"""