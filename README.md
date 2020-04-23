### MACAPI
Python script to query macaddress.io API and return the value associated with "Company name"

#### Requirements:
- Linux CLI only
- Implement the API from scratch, re-use of any libraries taking care of the query is not allowed
- Input: MAC address
- Output: "Company name" field
- Dockerized

#### How to build the container
```
$ docker build -t ccarmelo/macapi:1.1 .
```

#### How to run the container, example
```
$ docker run --rm --name macapi -e "APIKEY=${APIKEY}" ccarmelo/macapi:1.1 44:38:39:ff:ef:57
Cumulus Networks, Inc
```

#### How to get help
```
$ docker run --rm --name macapi ccarmelo/macapi:1.1 -h
usage: macapi.py [-h] [-V] [-v] <macaddr>

Search "Company name" based on input MAC address, version 1.1, build 20200423.

positional arguments:
  <macaddr>      MAC address

optional arguments:
  -h, --help     show this help message and exit
  -V, --verbose  verbose output
  -v, --version  show program's version number and exit
```

#### Security considerations
The API key has been removed from the application (initial version, line starting with "APIKEY...").
Now the API key must be exported as an environmental variable on the host running the container as `export APIKEY="***"`.

