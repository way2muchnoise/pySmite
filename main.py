__author__ = 'jens'


import session
import data
import smite


def print_indent(indent, text):
    for x in xrange(indent):
        text = " " + text
    print text

def print_dict(d, depth=0):
    if type(d) == dict:
        for k, v in d.items():
            if hasattr(v, '__iter__'):
                print_indent(depth, k)
                print_dict(v, depth+1)
            else:
                print_indent(depth, '%s : %s' % (k, v))
    elif type(d) == list:
        for v in d:
            if hasattr(v, '__iter__'):
                print_dict(v, depth+1)
            else:
                print_indent(depth, v)
    else:
        print_indent(depth, d)

s = session.create(data.dev_id, data.auth_key)
print_dict(smite.get_player(data.dev_id, data.auth_key, s.get_id(), 'way2muchnoise'))