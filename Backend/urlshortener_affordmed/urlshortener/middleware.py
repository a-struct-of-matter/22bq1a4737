import datetime

#this file contains middleware for logging requests and responses in the URL shortener application
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = datetime.datetime.now()
        response = self.get_response(request)
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        print(f"[{datetime.datetime.now()}] {request.method} {request.path} -> {response.status_code} [{duration:.4f}s]")
        return response
