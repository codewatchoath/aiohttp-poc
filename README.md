AioHTTP Proof of concept for status reporting to all nodes.

To setup:
* start virtualenv with `pipenv shell`
* install dependencies `pipenv install`
* start up to 3 servers (you can add more using the config.ini file)
  * `python server.py workstation1`
  * `python server.py workstation2`
  * `python server.py workstation3`
* Make a request to any server and get a response back from each one
* `GET http://localhost:8000`

Doing this request will print on `workstation's 1` shell:

    Success from workstation1
    Success from workstation2
    Success from workstation3

