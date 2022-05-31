import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Air Quality by City API! Supply params "/city/token"'

@app.route('/<city>/<token>')
def quote(city, token):

    quote_url = 'http://api.waqi.info/feed/{}/?token={}'.format(city, token)

    try:
        r = requests.get(quote_url)
        data = r.json()
        curr_aqi = data['data']['aqi']

        text = "{} latest air quality is {}".format(city, curr_aqi)

    except Exception:
        return data

    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# # test cases: api token is free so it doesn't matter about having it in plain text but would use a secrets manager instead in production
# result = quote('vancouver', 'token')
# print(result)
# result = quote('seattle', 'token')
# print(result)

# # handle error cases: return response
# # error case: invalid city
# result = quote('toront', 'token')
# print(result)
# # error case: invalid key
# result = quote('toronto', 'token')
# print(result)