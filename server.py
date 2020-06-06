from os import environ

environ['PYTHONIOENCODING'] = 'utf-8'

from http.server import HTTPServer, CGIHTTPRequestHandler

CGIHTTPRequestHandler.cgi_directories = ['/...']

server_address = ('', 8080)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print('Сервер запущен')

httpd.serve_forever()