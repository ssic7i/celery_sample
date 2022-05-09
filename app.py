from flask import Flask
from celery_worker import task1
import uuid

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    task_obj = task1.apply_async(args=[str(uuid.uuid4())])
    return str(task_obj)


if __name__ == '__main__':
    app.run()
