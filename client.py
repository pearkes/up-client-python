"""A client for github.com/pearkes/up-server.

Usage:
  upclient
  upclient list
  upclient add URL
  upclient info ID
  upclient delete ID
  upclient -h | --help
  upclient --version

Arguments:
  URL  url that you would like checked
  ID   the id of the url you would like to access directly

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
import requests
import json
import pprint

base_url = "http://localhost:4747"
headers = {"Content-Type": "application/json", "X-Up-Auth": "foo"}


def list_urls():
    "Lists all urls"
    r = requests.get(base_url + "/urls", headers=headers)
    return r.json, r.status_code


def add_url(url):
    "Adds a url"
    data = {"url": url}
    r = requests.post(base_url + "/url", data=json.dumps(data), headers=headers)
    return r.json, r.status_code


def get_url(id):
    "Get's a url"
    r = requests.get(base_url + "/url/%s" % id, headers=headers)
    return r.json, r.status_code


if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.1')
    if arguments.get("list"):
        pprint.pprint(list_urls())
    if arguments.get("add"):
        pprint.pprint(add_url(arguments["URL"]))
    if arguments.get("info"):
        pprint.pprint(get_url(arguments["ID"]))
