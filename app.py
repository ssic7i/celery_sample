import json
import os
import random

from flask import Flask, session, request

import database
import models
from celery_worker import task1
import uuid
import database

app = Flask(__name__)

session_secret = os.environ.get('SESSION_SECRET')
if not session_secret:
    if not os.path.exists('session.secret'):
        secret_file = open('session.secret', 'w')
        secret_file.write(str(random.randint(10000000, 999999999)))
        secret_file.close()
    secret_file = open('session.secret')
    session_secret = secret_file.read()
    secret_file.close()

app.secret_key = session_secret


@app.route('/')
def hello_world():  # put application's code here
    task_obj = task1.apply_async(args=[str(uuid.uuid4())])
    return str(task_obj)
@app.route('/add')
def endpoint1():
    database.init_db()
    unique_user = uuid.uuid4()
    user1 = models.User(name=f'{unique_user}', email=f'{unique_user}@example.com')
    database.db_session.add(user1)
    database.db_session.commit()
    return f'{unique_user}'

@app.route('/session', methods=['GET', 'POST', 'DELETE'])
def session_endpoint():
    req_args = dict(request.args)
    if request.method == 'POST':
        for key, value in req_args.items():
            session[key] = value
        return json.dumps(dict(session))
    elif request.method == 'DELETE':
        for key, value in req_args.items():
            session.pop(key)
    return json.dumps(dict(session))

@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()

if __name__ == '__main__':
    app.run()
