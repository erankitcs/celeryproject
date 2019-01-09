from __future__ import absolute_import
from celery import Celery
import time

#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks',
             broker='amqp://',
             backend='rpc://',
             include=['tasks'])

@app.task
def add(x, y):
    print
    'long time task begins'
    # sleep 5 seconds
    time.sleep(5)
    print
    'long time task finished'
    return x + y

