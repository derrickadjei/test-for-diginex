import os
import json
import requests
from random import seed, random
from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(err):
    code = 500
    if isinstance(err, HTTPException):
        code = err.code
    return jsonify(error=str(err)), code


URL = "http://127.0.0.1:5000/reverse"  # url of reverse api app
seed(1)  # seeding random generator


@app.route('/servicetwo', methods=['POST'])
def reverse():
    data = json.loads(request.data)
    for keyvalue in data:
        if "messages" in keyvalue:
            value = data.get('messages')  # reading from requests
            req = {"messages": val}  # payload
            payload = json.dumps(req)
            headers = {
                'content-type': "application/json",
            }
            response = requests.request(
                "POST", URL, data=payload, headers=headers)
            get_req = {}
            get_req = response.json()
            get_req.update({"rand": random()})
            return json.dumps(get_req)

        return abort(500, "invalid request received")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)