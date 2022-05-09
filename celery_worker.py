import datetime
import time

from celery import Celery

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')



@app.task
def task1(some_uuid):
    start_time = datetime.datetime.now()
    time.sleep(10)
    end_time = datetime.datetime.now()
    file_obj = open('tasks.txt', 'a')
    file_obj.write(f'uuid: {some_uuid} start time: {start_time}, end time: {end_time}\r\n')
    file_obj.close()
    return True