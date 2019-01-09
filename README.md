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

Celery is on the Python Package Index (PyPI), so it can be installed with standard Python tools like pip or easy_install:

$ pip install celery


---D:\Study\Python\Projects\celeryproject\celeryproject\venv\Lib\site-packages\celery\backends  --> Change async file name to asynchronous

---Change rpc.py ---> import statement from async to asynchronous



