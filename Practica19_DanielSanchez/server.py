from http.server import  BaseHTTPRequestHandler, HTTPServer

class http_server:
    def __init__(self):
        server = HTTPServer(('', 8087), myHandler)
        server.serve_forever()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):


        if ("practica" in self.requestline):
            f = open("practica.html")
            r = f.read()
            print (r)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            self.wfile.write(bytes(r, 'utf8'))
        else:
            self.send_error(404)

            self.wfile.write(bytes("<html><head><title>Example</title></head><body><p>" + self.requestline + " 404 Not Found</p></body></html>", 'utf8'))

        # Hacer lo que queramos con la petición
        return

class main:
    def __init__(self):

        self.server = http_server()

if __name__ == '__main__':
    m = main()
