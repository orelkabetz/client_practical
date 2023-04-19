from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/test_get_method')
def send_data_using_query_parameters():
    id = request.args.get('id')
    year = request.args.get('year')
    # generate a random response string
    response_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789-', k=20))
    return response_string


@app.route('/test_post_method', methods=['POST'])
def sending_data_to_the_server_using_a_body():
    response_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789-', k=20))
    response = {'message': response_string}
    return jsonify(response)


@app.route('/test_put_method', methods=['PUT'])
def update_data_in_the_server():
    response_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789-', k=20))
    response = {'message': response_string}
    return jsonify(response)


@app.route('/test_delete_method', methods=['DELETE'])
def delete_resource():
    pass


if __name__ == '__main__':
    app.run(port=8989)
