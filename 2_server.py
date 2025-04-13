from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


# Creating the Server to Hanfle the requests

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        if 'code' in params:
            code = params['code'][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Authorization Code: {code}".encode())
            print(f"\n✅ Received Authorization Code:\n{code}")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing code parameter.")

print("🚀 Starting server at http://localhost:8080 ...")
server = HTTPServer(('localhost', 8080), Handler)
server.serve_forever()
