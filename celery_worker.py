import datetime
import time

from celery import Celery

import database
import models

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')



@app.task
def task1(some_uuid):
    database.init_db()
    start_time = datetime.datetime.now()
    time.sleep(10)
    end_time = datetime.datetime.now()
    file_obj = open('tasks.txt', 'a')
    file_obj.write(f'uuid: {some_uuid} start time: {start_time}, end time: {end_time}\r\n')
    file_obj.close()

    user1 = models.User(name=f'{some_uuid}', email=f'{some_uuid}@example_celery.com')
    database.db_session.add(user1)
    database.db_session.commit()

    database.db_session.remove()
    return True