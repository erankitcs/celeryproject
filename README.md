# celeryproject
A Practical Guide to the Celery Distributed Task Queue

Celery is a asynchronous task queue/job queue based on distributed message passing.
It is focused on real time but it can be scheduled one as well.

Basic unit of Celery is Tasks which are executed concurrently on single or more worker servers using multiprocessing.

Task can be executed in background(asynchronous) or wait until ready(synchronous).

Task queues are used as a mechanism to distribute work across threads or machines.

Dedicated worker processes constantly monitor task queues for new work to perform. Celery communicates via messages usually using a broker
to mediate  between clients and workers.

To initiates a task, usually client adds a message to the queue, broker then delivers that message to a worker.

Hence, Celery needs a message transport to send and recieve messages.The RabbitMQ and Redis broker transports are feature complete, but there’s others 
also.
 
Celery can run on a single machine, on multiple machines, or even across data centers.

GETTING STARTED
Install celery by download or 

pip install -U Celery

Set up RabbitMQ, Redis or one of the other supported brokers.

----Installing RabbitMQ : 

RabbitMQ requires a 64-bit supported version of Erlang for Windows to be installed.

Download Erlang from below link:
http://www.erlang.org/downloads

Erlang installer must be run using an administrative account otherwise a registry key expected by the RabbitMQ installer will not be present.

Then, run the RabbitMQ installer, rabbitmq-server-3.7.9.exe. It installs RabbitMQ as a Windows service and starts it using the default configuration.

To stop the broker or check its status, use rabbitmqctl.bat in sbin (as an administrator).

Stopping the Node     ==> rabbitmqctl.bat stop
Checking Node Status  ==> rabbitmqctl.bat status

Seeting Up RabbitMQ : 

D:\Study\rabbitmq_server-3.7.9\sbin>rabbitmqctl.bat add_user ankit ankit123
Adding user "ankit" ...

D:\Study\rabbitmq_server-3.7.9\sbin>rabbitmqctl.bat add_vhost ankit_vhost
Adding vhost "ankit_vhost" ...

D:\Study\rabbitmq_server-3.7.9\sbin>rabbitmqctl.bat set_user_tags ankit ankit_tag
Setting tags for user "ankit" to [ankit_tag] ...

D:\Study\rabbitmq_server-3.7.9\sbin>rabbitmqctl.bat set_permissions -p ankit_vhost ankit ".*" ".*" ".*"
Setting permissions for user "ankit" in vhost "ankit_vhost" ...



Celery is on the Python Package Index (PyPI), so it can be installed with standard Python tools like pip or easy_install:

$ pip install celery

---Fix for the issue : 
---D:\Study\Python\Projects\celeryproject\celeryproject\venv\Lib\site-packages\celery\backends  --> Change async file name to asynchronous

---Change rpc.py ---> import statement from async to asynchronous


Running a worker Process: 

celery -P solo -A tasks worker --loglevel=info

There is bug into celery where it is not able to specify worker class automatically hence passing it through startup command: -P solo


Running a test script: 

(venv) D:\Study\Python\Projects\celeryproject\celeryproject>python  Test.py
Task finished?  False
Task result:  None
Task finished?  True
Task result:  101

(venv) D:\Study\Python\Projects\celeryproject\celeryproject>

You can install Flower as well and keep tracking your request.

>pip install flower

Starting flower:

(venv) D:\Study\Python\Projects\celeryproject\celeryproject>celery -A tasks flower
[I 190109 21:45:23 command:139] Visit me at http://localhost:5555
[I 190109 21:45:23 command:144] Broker: amqp://guest:**@localhost:5672//
[I 190109 21:45:23 command:147] Registered tasks:
    ['celery.accumulate',
     'celery.backend_cleanup',
     'celery.chain',
     'celery.chord',
     'celery.chord_unlock',
     'celery.chunks',
     'celery.group',
     'celery.map',
     'celery.starmap',
     'tasks.add']
[I 190109 21:45:23 mixins:224] Connected to amqp://guest:**@127.0.0.1:5672//



 



