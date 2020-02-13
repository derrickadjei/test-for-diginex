import json
from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


# the HTTPException check ensures that the status code is preserved
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

#API post request
@app.route('/reverse', methods=['POST'])
def reverse():
    data = json.loads(request.data)
    for keyvalue in data:
        if "message" in keyvalue:
            val = data.get('message')[::-1]
            return_data = {"message": val}
            return json.dumps(return_data)

        # json.dumps("invalid request received")
        return abort(500, "invalid request received")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)