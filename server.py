from webob import Request
req = Request.blank('http://localhost/test')
resp = req.get_response(application)
print resp
