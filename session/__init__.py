__author__ = 'way2muchnoise'

import hashlib
import datetime
import request
import smite


class Session():
    def __init__(self, json):
        self.id = json['session_id']

    def get_id(self):
        return self.id


def get_signature(dev_id, method_name, auth_key, timestamp):
    return hashlib.md5(dev_id + method_name + auth_key + timestamp).hexdigest()


def create(dev_id, auth_key):
    method_name = "createsession"
    response_format = "json"
    timestamp = get_timestamp()
    return Session(
        request.json(
            smite.base_url
            + method_name
            + response_format + "/"
            + dev_id + "/"
            + get_signature(dev_id, method_name, auth_key, timestamp) + "/"
            + timestamp
        ))


def get_timestamp():
    return datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')


def test_session(session_id, dev_id, auth_key):
    method_name = "testsession"
    response_format = "json"
    timestamp = get_timestamp()
    return request.json(
        smite.base_url
        + method_name
        + response_format + "/"
        + dev_id + "/"
        + get_signature(dev_id, method_name, auth_key, timestamp) + "/"
        + session_id + "/"
        + timestamp
    )