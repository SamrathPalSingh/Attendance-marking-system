#starts the http server for the student webpage

import http.server
import socketserver
global httpd
def startServer():
    global httpd
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port"+ str(PORT) )
    httpd.serve_forever()
def stopServer():
    global httpd
    httpd.server_close()
