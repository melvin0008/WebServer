from webob import Request
from webob import exc
import re

var_regex = re.compile(r'''\{ (\w+)(?::([^}]+))? \}''', re.VERBOSE)

#split route urls to regex
def url_template_to_regex(url_template):
     regex = ''
     last_pos = 0
     for match in var_regex.finditer(url_template):
         regex += re.escape(url_template[last_pos:match.start()])
         var_name = match.group(1)
         expr = match.group(2) or '[^/]+'
         expr = '(?P<%s>%s)' % (var_name, expr)
         regex += expr
         last_pos = match.end()
     regex += re.escape(url_template[last_pos:])
     regex = '^%s$' % regex
     return regex

