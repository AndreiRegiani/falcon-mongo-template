# REST API with Falcon, MongoDB and PyPy

Project Template for a high-performance RESTful web service in Python.


## Setup

```
virtualenv -p /usr/bin/pypy env
source env/bin/activate
pip install -r requirements.txt
```


## Run Development Server

```
./run_server.sh
```
Listening at http://localhost:8000. `Gunicorn` is used as WSGI HTTP Server.
