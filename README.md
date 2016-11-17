# REST API with Falcon, MongoDB and PyPy

Project Template for a high-performance RESTful web service in Python.


## Setup

* Install [PyPy](http://pypy.org/) (or just use `Python 2.7`) and [MongoDB](https://www.mongodb.com/)
* Check database credentials at `src/settings.py`
* Install dependencies on a `virtualenv`:

```
virtualenv -p /usr/bin/pypy env
source env/bin/activate
pip install -r requirements.txt
```


## Run Development Server

```
./run_server.sh
```
Listening at [localhost:8000](http://localhost:8000). `Gunicorn` is used as WSGI HTTP Server.

**Demo routes:**

* `POST /api/example  {"email": "value"}` create an item
* `GET  /api/example` return all items


## Further Reading

* [MongoEngine Docs](http://docs.mongoengine.org/)
* [Falcon Docs](https://falcon.readthedocs.io/en/stable/)
* [Gunicorn Docs](http://docs.gunicorn.org/en/stable/)
* [About PyPy](http://pypy.org/features.html)
