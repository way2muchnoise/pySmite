__author__ = 'jens'

import session
import request

base_url = 'http://api.smitegame.com/smiteapi.svc/'

def get_player(dev_id, auth_key, session_id, name):
    method_name = "getplayer"
    response_format = "json"
    timestamp = session.get_timestamp()
    return request.json(
            base_url
            + method_name
            + response_format + "/"
            + dev_id + "/"
            + session.get_signature(dev_id, method_name, auth_key, timestamp) + "/"
            + session_id + "/"
            + timestamp + "/"
            + name
        )