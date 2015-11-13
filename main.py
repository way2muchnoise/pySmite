__author__ = 'way2muchnoise'

import session
import data
import smite
import smite.params


def print_indent(indent, text):
    for x in xrange(indent):
        text = " " + text
    print text


def print_dict(d, depth=0):
    if type(d) == dict:
        for k, v in d.items():
            if hasattr(v, '__iter__'):
                print_indent(depth, k)
                print_dict(v, depth + 1)
            else:
                print_indent(depth, '%s : %s' % (k, v))
    elif type(d) == list:
        for v in d:
            if hasattr(v, '__iter__'):
                print_dict(v, depth + 1)
            else:
                print_indent(depth, v)
    else:
        print_indent(depth, d)


def get_player_ranks(player_name):
    player_status = smite.get_player_status(data.dev_id, data.auth_key, s.get_id(), player_name)
    if player_status[0]['status'] == 2:
        print player_name + ' is in Pick and Bans'
        raw_input('Press enter to retry...')
        get_player_ranks(player_name)
    elif player_status[0]['status'] == 3:
        match = smite.get_match_player_details(data.dev_id, data.auth_key, s.get_id(), player_status[0]['Match'])
        teams = [[], []]
        for player in match:
            league = smite.get_player_league(data.dev_id, data.auth_key, s.get_id(), player['playerName'])
            teams[player['taskForce'] - 1].append('%s (%s) : %s' % (player['playerName'], player['GodName'], league))
        print smite.params.get_game_mode(match[0]['Queue'])
        print 'Team 1:'
        for player in teams[0]:
            print ' ' + player
        print 'Team 2:'
        for player in teams[1]:
            print ' ' + player
    else:
        print player_name + " is not in a game or lobby"


s = session.create(data.dev_id, data.auth_key)
player_name = raw_input('Give a player name:')
get_player_ranks(player_name)
