from flask import Flask, url_for, request
from collections import defaultdict
app = Flask(__name__)

USERS_PWD = {"glen": "1234", "hq": "password"}
MESSAGES = defaultdict(list)

def authenticate():
    if not request.authorization:
        return False
    username = request.authorization.username
    password = request.authorization.password
    return USERS_PWD[username] == password

# Posted message has body with keys
# target - target user
# body - message body

@app.route('/message/<username>', methods = ['POST'])
def post_message(username):
    if authenticate():
        message_body = request.form["body"]
        MESSAGES[username].append(message_body)
        print MESSAGES
        return "{0} successfully sent to {1}".format(message_body, username)
    else:
        return "Message sending unsuccessful"

@app.route('/retrieve')
def get_message():
    if authenticate():
        message_list = MESSAGES[request.authorization.username]
        MESSAGES[request.authorization.username] = []
        return str(message_list)

if __name__ == "__main__":
    app.run(ssl_context=("server.crt", "server.key"))
# @app.route('/register')
