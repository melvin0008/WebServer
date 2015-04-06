from webob import Request

def application(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello World!']

req = Request.blank('http://localhost/test')
resp = req.get_response(application)


if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port=8080)
