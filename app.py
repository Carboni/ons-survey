import os
from flask import Flask, request, jsonify

app = Flask(__name__)


access_codes = {"1": "ACME Corporation", "2": "Methods Digital", "3": "People Thinking"}


@app.route("/")
def hello():
    all_args = request.args.to_dict()
    return jsonify(all_args)


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


@app.route('/profile', methods=['POST'])
def upsert():
    profile = request.get_json()

    if not profile:
        return known_error("Request payload was empty")

    app.logger.debug("profile: " + repr(profile))

    return jsonify(profile)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
