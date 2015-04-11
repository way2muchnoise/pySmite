__author__ = 'jens'

import session
import request
import params
import urllib2

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
        + urllib2.quote(name.encode('utf8'))
    )


def get_match_player_details(dev_id, auth_key, session_id, match_id):
    method_name = "getmatchplayerdetails"
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
        + repr(match_id)
    )


def get_player_status(dev_id, auth_key, session_id, name):
    method_name = "getplayerstatus"
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
        + urllib2.quote(name)
    )


def get_player_league(dev_id, auth_key, session_id, name):
    player = get_player(dev_id, auth_key, session_id, name)[0]
    return params.get_league_tier(player['Tier_Conquest'])


def get_player_league_with_elo(dev_id, auth_key, session_id, name):
    player = get_player(dev_id, auth_key, session_id, name)[0]
    return params.get_league_tier(player['Tier_Conquest']) + " " + repr(round(player['Rank_Stat']))[:-2]