from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        requests.post("http://decision-service:7000/save", request.form)
   
    return '''
    <!doctype html>
    <head>
    <title>Flask App</title>
    </head>
    <body>
    <h1>Save key-value pair to redis</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name=key placeholder=key>
      <input type=text name=value placeholder=value>
      <input type=submit value='save to redis'>
    </form>
    <a href="/keys"> get keys from redis</a>   
    </body>
    '''
    
@app.route('/keys', methods=['GET'])
def get_keys():
    res = requests.get("http://decision-service:7000/keys")
    return res.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
