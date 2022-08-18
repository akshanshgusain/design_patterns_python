from typing import DefaultDict

from structural.proxy.application import Application
from structural.proxy.iServer import Server

"""
The proxy object has the same interface as a service, which makes it interchangeable with a real object when passed to a client.
"""
"""
Proxy is a structural design pattern that provides an object that acts as a substitute for a real service object
used by a client. A proxy receives client requests, does some work (access control, caching, etc.) and then passes
the request to a service object.
"""


class Nginx(Server):
    # = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

    def __init__(self,
                 application: Application,
                 max_allowed_requests: int,
                 supported_methods: list[str]):
        self.application = application
        self.max_allowed_requests = max_allowed_requests
        self.rate_limiter: DefaultDict[str: int] = {}
        self.supported_methods: list[str] = supported_methods

    def check_rate_limiting(self, url: str) -> bool:
        if url in self.rate_limiter:
            if self.rate_limiter.get(url, 0) > self.max_allowed_requests:
                return False
            else:
                self.rate_limiter[url] = self.rate_limiter.get(url, 0) + 1
                return True
        else:
            self.rate_limiter[url] = 1
            return True

    def check_method_allowed(self, method: str) -> bool:
        if method in self.supported_methods:
            return True
        else:
            return False

    def handle_request(self, url: str, method: str) -> dict:
        allowed: bool = self.check_rate_limiting(url)
        if not allowed:
            return {"status_code": 429, "message": "Too Many Requests"}

        method_allowed: bool = self.check_method_allowed(method)
        if not method_allowed:
            return {"status_code": 405, "message": "Method Not Allowed"}

        return self.application.handle_request(url, method)
