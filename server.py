import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = "."

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]
        
        if path == '/':
            self.path = '/index.html'
        elif not os.path.splitext(path)[1]:
            html_path = path + '.html'
            if os.path.exists('.' + html_path):
                self.path = html_path
        
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), CleanURLHandler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT}")
        httpd.serve_forever()
