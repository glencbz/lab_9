import requests

USERNAME = "glen"
PASSWORD = "1234"
AUTH = (USERNAME, PASSWORD)
URL = "https://localhost:5000/"

MESSAGE_ENDPOINT = "message/"
RETRIEVE_ENDPOINT = "retrieve"

def send_message(target, message_body):
    message_url = URL + MESSAGE_ENDPOINT + target
    data = {"body": message_body}
    print requests.post(message_url, data=data, auth=AUTH, verify="server.crt").content

def retrieve_messages():
    retrieve_url = URL + RETRIEVE_ENDPOINT
    print requests.get(retrieve_url, auth=AUTH, verify="server.crt").content

send_message("glen", "hi")
send_message("glen", "hello")
send_message("glen", "y u no respond")
retrieve_messages()