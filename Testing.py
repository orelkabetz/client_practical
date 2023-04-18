from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TARGET_SERVER = "localhost"
TARGET_PORT = "8989"
BASE_URL = f"http://{TARGET_SERVER}:{TARGET_PORT}"


@app.route('/test_get_method', methods=['GET'])
def test_get_method():
    id = request.args.get('id')
    year = request.args.get('year')


@app.route('/test_post_method', methods=['PUT'])
def test_post_method(requestId):
    print("sendDataUsingBody - ", requestId)
    dataToSend = {
        "id": 315668954,
        "year": 1996,
        "requestId": 'qo-4xchuzcdpsblhc0rf'
    }
    # response = requests.post(f"{BASE_URL}/test_post_method", json=dataToSend)
    jsonData = response.json()
    print(jsonData)
    messageId = jsonData['message']
    return messageId


@app.route('/test_put_method', methods=['PUT'])
def test_put_method():
    id = request.args.get('id')
    data = request.get_json()
    return jsonify(message=id)


@app.route('/test_delete_method', methods=['DELETE'])
def test_delete_method():
    id = request.args.get('id')
    return jsonify(message=f"Deleted id: {id}")


def run():
    response = requests.get(f"{BASE_URL}/test_get_method?id=312198179&year=1994")
    requestId = response.text
    test_post_method(requestId)
    # postMessage = requests.post(f"{BASE_URL}/test_post_method")
    # , json={'requestId': requestId}).json()['message']
    updatedMessageId = requests.put(f"{BASE_URL}/test_put_method?id={postMessage}", json={'id': (315668954 - 294234) % 34, 'year': (1996 + 94) % 13}).json()['message']
    requests.delete(f"{BASE_URL}/test_delete_method?id={updatedMessageId}")
    return "Done"


if __name__ == '__main__':
    # app.run(debug=True)
    run()
