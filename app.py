import os
from flask import Flask, request, jsonify
from access_codes import access_codes
from flask_cors import CORS


# Set up the app with cross-origin resource sharing enabled:
app = Flask(__name__)
CORS(app)


@app.route("/code")
def check_code():
    query_args = request.args.to_dict()
    result = "Test"
    if "access_code" in query_args:
        access_code = query_args["access_code"]
        if access_code in access_codes:
            result = access_codes[access_code]
        else:
            return known_error("Unknown access code: " + access_code + ".")
    else:
        return known_error("Please supply an 'access_code' query parameter.")
    return jsonify(result)


@app.route("/codes")
def list_codes():
    return jsonify(access_codes)


@app.errorhandler(400)
def known_error(error=None):
    app.logger.error("FAILURE '%s'", request.data.decode('UTF8'))
    message = {
        'status': 400,
        'message': "{}: {}".format(error, request.url),
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.errorhandler(500)
def unknown_error(error=None):
    app.logger.error("FAILURE '%s'", request.data.decode('UTF8'))
    message = {
        'status': 500,
        'message': "Internal server error: " + repr(error),
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
