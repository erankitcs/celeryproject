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
    print('Wait time  begins')
    # sleep 5 seconds
    time.sleep(5)
    print('5 sec wait time  finished')
    return x + y

