#!/usr/bin/env python

from bottle import route, run, static_file, view

visitors = 0

""" Turn the visitor count into a nice string (1st, 2nd, 3rd etc. ). """
def get_visitor_index(visitors):
    suffix = ''
    if visitors in [11, 12, 13]:
        suffix = 'th'
    else:
        last_digit = visitors % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return '%d%s' % (visitors, suffix)

""" Root page with visitor counter. """
@route('/')
@view('root')
def root():
    global visitors
    visitors += 1
    visitor_index = get_visitor_index(visitors)
    return dict(visitor_index = visitor_index)

""" Serve static files. """
@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='static')

run(host='localhost', port=8080)
