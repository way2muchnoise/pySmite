__author__ = 'jens'


import urllib2
import json as json_reader


def json(url):
    return json_reader.load(urllib2.urlopen(url))
