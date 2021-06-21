import http.server
import random
from prometheus_client import start_http_server, Counter

APP_PORT = 8000
METRICS_PORT = 8001

REQUEST_COUNTER = Counter(name="my_app_request_counter",documentation="Keep Track of Request Counts", labelnames=['method'])
RANDOM_COUNTER = Counter(name="my_app_random_counter",documentation="Keep Track of Random Counts", labelnames=['method', 'type'])

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        REQUEST_COUNTER.labels('GET').inc()
        ran = random.random() * 10
        RANDOM_COUNTER.labels('GET', 'Random').inc(ran)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application of.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('127.0.0.1', APP_PORT), HandleRequests)
    server.serve_forever()