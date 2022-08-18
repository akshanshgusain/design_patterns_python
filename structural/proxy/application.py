from structural.proxy.iServer import Server


class Application(Server):

    def handle_request(self, url: str, method: str) -> dict:
        if url == "/app/status" and method == "GET":
            return {"status_code": 200, "message": "Ok"}

        if url == "/create/user" and method == "POST":
            return {"status_code": 201, "message": "User created"}

        return {"status_code": 404, "message": "Not Found"}
