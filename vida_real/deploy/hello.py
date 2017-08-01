"""
WSGI deploy application Hello World
"""


def application(enviroment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello World!']
