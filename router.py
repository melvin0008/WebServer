from webob import Request
from webob import exc
class Router(object):
      def __init__(self):
          self.routes = []

      def add_route(self, template, controller, **vars):

      def __call__(self, environ, start_response):
