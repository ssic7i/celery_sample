from flask import Flask

import database
import models
from celery_worker import task1
import uuid
import database

app = Flask(__name__)


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

@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()

if __name__ == '__main__':
    app.run()
