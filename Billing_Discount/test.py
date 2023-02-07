from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/abc', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        item1 = float(request.json['item1'])
        item2 = float(request.json['item2'])
        item3 = float(request.json['item3'])
        item4 = float(request.json['item4'])
        item5 = float(request.json['item5'])

        total_cost = item1 + item2 + item3 + item4 + item5

        if total_cost <= 10:
            final_bill = total_cost - (total_cost * 0.1)
        elif 1000 < total_cost <= 2000:
            final_bill = total_cost - (total_cost*0.2)
        else:
            final_bill = total_cost - (total_cost*0.3)

        return f"Total billing after discount: {final_bill}"


if __name__ == "__main__":
    app.run()

