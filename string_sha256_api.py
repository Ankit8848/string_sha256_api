from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)


@app.route('/convert', methods=['GET', 'POST'])
def string_to_sha256():
    data = request.get_json()
    if 'string' not in data:
        return jsonify({'error': 'Missing "string" field in JSON request'}), 400

    input_string = data['string']
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()

    response_data = {
        'input_string': input_string,
        'sha256_hash': sha256_hash
    }

    return jsonify(response_data), 200


def myEndpoint():
    requestJson = request.get_json(force=True)

    return requestJson


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=True)
