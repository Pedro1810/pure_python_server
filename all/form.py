#!python

######### Ставим cookie
from http import cookies
import os

cook = cookies.SimpleCookie()
cook['name'] = 'John'
cook['name']['path'] = '/'

import time

expires = time.gmtime(time.time() + 600)
expires = time.strftime('%a, %d, %b %Y %T GMT', expires)
cook['name']['expires'] = expires
cook['name']['httponly'] = 1

print(cook.output())
print()
print('OK')
######## Читаем cookie
cook = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
print(cook.get('name').value)

# qs = os.environ.get('QUERY_STRING')
# qs = qs.split('&')
# for item in qs:
# key, value = item.split('=')
# import cgi

# params = cgi.FieldStorage()

# name = params.getvalue('name', 'Guest')
# age = params.getvalue('age', '-')

# print('Content-Type: text/html')
# print('Set-Cookie: name=' + name)
# print()
# print('Name: ' + name + '<br>')
# print('Age: ' + age + '<br>')

# import os, sys

# if os.getenv('QUERY_STRING'):
# qs = os.getenv('QUERY_STRING')
# elif os.getenv('HTTP_METHOD') == 'POST':
# args = sys.stdin.read()