
from unicodedata import decimal
import requests
import json

from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template("obsluga_api.html", rates=get_rates())
    elif request.method == 'POST':
        print(request.form)
        code = request.form['currency']
        amount = float(request.form['amount'])
        rate = {}
        for item in get_rates():
            if item['code'] == code:
                rate = item
        result = float(round(rate['bid'], 2)) * amount
        return render_template("obsluga_api.html", rates=get_rates(), result=result)

def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    data_as_json = json.dumps(data)
    data_from_json = json.loads(data_as_json)
    rates = data_from_json[0]["rates"]
    return rates


