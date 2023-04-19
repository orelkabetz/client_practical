import json
import requests

HOST = 'http://localhost:8989'
ID_VALUE = 312198179
YEAR_VALUE = 1994


def send_data_using_query_parameters():
    url = f'{HOST}/test_get_method?id={ID_VALUE}&year={YEAR_VALUE}'
    response = requests.get(url)
    return response.text if response.status_code == 200 else None


def sending_data_to_the_server_using_a_body(request_id):
    url = f'{HOST}/test_post_method'
    data = {
        "id": str(ID_VALUE),
        "year": str(YEAR_VALUE),
        "requestId": request_id
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    json_data = response.json()
    if 'message' in json_data and response.status_code == 200:
        return json_data['message']
    else:
        return None


def update_data_in_the_server(post_message):
    id_value = (ID_VALUE - 294234) % 34
    year_value = (YEAR_VALUE + 94) % 13
    url = f'{HOST}/test_put_method'
    query_params = dict(id=post_message)
    data = {
        'id': id_value,
        'year': year_value
    }
    json_data = json.dumps(data)
    response = requests.put(url, json=json_data, params=query_params)
    json_data = response.json()
    if 'message' in json_data and response.status_code == 200:
        return json_data['message']
    else:
        return None


def delete_resource(updated_message_id):
    url = f'{HOST}/test_delete_method?id={updated_message_id}'
    response = requests.delete(url)
    return None


def run():
    request_id = send_data_using_query_parameters()
    post_message = sending_data_to_the_server_using_a_body(request_id)
    updated_message_id = update_data_in_the_server(post_message)
    delete_resource(updated_message_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
