from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

app = Flask(__name__)

payload = "hello from decision service"

@app.route('/')
def hello():
    return payload

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        global payload
        payload = request.form
        
        redis.set(payload["key"], payload["value"])
        
    return payload, 200

@app.route('/keys', methods=['GET'])
def get_values_from_redis():
    return str(redis.keys())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
