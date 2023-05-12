from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverport = 8080


class Myserver(BaseHTTPRequestHandler):

   def do_GET(self):
       self.send_response(200)
       self.send_header("Content-type", "application/json")
       self.end_headers()
       self.wfile.write(bytes('Hello, World wide web!', "utf-8"))



if __name__ == "__main__":
    webserver = HTTPServer((hostname, serverport), Myserver)
    print("Server started http://%s:%s" % (hostname, serverport))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")