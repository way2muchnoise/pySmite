__author__ = 'way2muchnoise'

import session
import request
import params
import urllib2

base_url = 'http://api.smitegame.com/smiteapi.svc/'
xbox_url = 'http://api.xbox.smitegame.com/smiteapi.svc'
ps4_url = 'http://api.ps4.smitegame.com/smiteapi.svc'


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


def get_player_id(dev_id, auth_key, session_id, player_name):
    return get_player(dev_id, auth_key, session_id, player_name)[0]['Id']


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
    level = player['Level']
    if level < 30:
        return 'Level ' + repr(level)
    games = player['LeagueConquest']['Wins'] + player['LeagueConquest']['Losses']
    if player['Tier_Conquest'] > 1 or games > 9:
        return params.get_league_tier(player['Tier_Conquest'])
    else:
        return 'Qualifying ' + games + '/10 '


def get_player_league_with_elo(dev_id, auth_key, session_id, name):
    player = get_player(dev_id, auth_key, session_id, name)[0]
    level = player['Level']
    if level < 30:
        return 'Level ' + repr(level)
    games = player['LeagueConquest']['Wins'] + player['LeagueConquest']['Losses']
    if player['Tier_Conquest'] > 1 or games > 9:
        return params.get_league_tier(player['Tier_Conquest']) + " " + repr(round(player['Rank_Stat']))[:-2]
    else:
        return 'Qualifying ' + repr(games) + '/10 ' + repr(round(player['Rank_Stat']))[:-2]


def get_god_ranks(dev_id, auth_key, session_id, player_name):
    method_name = "getgodranks"
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
        + urllib2.quote(player_name)
    )


def get_clan_player(dev_id, auth_key, session_id, name):
    method_name = "getteamplayers"
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


def get_friends(dev_id, auth_key, session_id, name):
    method_name = "getfriends"
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


def get_items(dev_id, auth_key, session_id, lang=params.langCode['English']):
    method_name = "getitems"
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
        + lang
    )


def get_gods(dev_id, auth_key, session_id, lang=params.langCode['English']):
    method_name = "getgods"
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
        + repr(lang)
    )


def get_god_id(dev_id, auth_key, session_id, god_name, lang=params.langCode['English']):
    gods = get_gods(dev_id, auth_key, session_id, lang)
    for god in gods:
        if unicode.lower(god["Name"]) == str.lower(god_name):
            return god["id"]
    return -1


def get_god_skins(dev_id, auth_key, session_id, god_name, lang=params.langCode['English']):
    method_name = "getgodskins"
    response_format = "json"
    god_id = get_god_id(dev_id, auth_key, session_id, god_name, lang)
    timestamp = session.get_timestamp()
    return request.json(
        base_url
        + method_name
        + response_format + "/"
        + dev_id + "/"
        + session.get_signature(dev_id, method_name, auth_key, timestamp) + "/"
        + session_id + "/"
        + timestamp + "/"
        + repr(god_id) + "/"
        + repr(lang)
    )


def search_clans(dev_id, auth_key, session_id, search):
    method_name = "searchteams"
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
        + urllib2.quote(search)
    )


def get_achievements(dev_id, auth_key, session_id, player_name):
    method_name = "getplayerachievements"
    response_format = "json"
    player_id = get_player_id(dev_id, auth_key, session_id, player_name)
    timestamp = session.get_timestamp()
    return request.json(
        base_url
        + method_name
        + response_format + "/"
        + dev_id + "/"
        + session.get_signature(dev_id, method_name, auth_key, timestamp) + "/"
        + session_id + "/"
        + timestamp + "/"
        + repr(player_id)
    )


def get_esports_details(dev_id, auth_key, session_id):
    method_name = "getesportsproleaguedetails"
    response_format = "json"
    timestamp = session.get_timestamp()
    return request.json(
        base_url
        + method_name
        + response_format + "/"
        + dev_id + "/"
        + session.get_signature(dev_id, method_name, auth_key, timestamp) + "/"
        + session_id + "/"
        + timestamp
    )


def get_patch_info(dev_id, auth_key):
    method_name = "getpatchinfo"
    response_format = "json"
    timestamp = session.get_timestamp()
    return request.json(
        base_url
        + method_name
        + response_format + "/"
        + dev_id + "/"
        + session.get_signature(dev_id, method_name, auth_key, timestamp) + "/"
        + timestamp
    )
