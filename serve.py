import http.server
import socketserver
import webbrowser
import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    url = f"http://localhost:{PORT}/index.html"
    print(f"Membuka Mutual Fund Web Dashboard di {url} ...")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Gagal membuka browser otomatis: {e}")
        
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server berjalan di {url}. Tekan Ctrl+C untuk menghentikan server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")
