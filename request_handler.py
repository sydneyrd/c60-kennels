import json
from repository import all, single, create, delete, update
from http.server import BaseHTTPRequestHandler, HTTPServer
# from views import (get_all_animals, get_single_animal, update_customer, update_employee, update_location, update_animal, get_single_location, delete_location, delete_animal, delete_customer, delete_employee, get_all_locations, get_all_employees, delete_animal, get_single_employee,
# get_all_customers, get_single_customer, create_animal, create_location, create_customer, create_employee)

method_mapper = {
    "animals": {
        "all": all,
        "single": single,
        "create": create,
        "update": update,
        "delete": delete
    },
    "locations": {
        "all": all,
        "single": single,
        "create": create,
        "update": update,
        "delete": delete
    },
    "employees": {
        "all": all,
        "single": single,
        "create": create,
        "update": update,
        "delete": delete
    },
    "customers": {
        "all": all,
        "single": single,
        "create": create,
        "update": update,
        "delete": delete
    }
}


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/
        return (resource, id)  # This is a tuple
    def get_all_or_single(self, resource, id):
        if id is not None:   
            response = method_mapper[resource]["single"](resource, id)
            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = {"error": "Not Found"}
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"](resource)

        return response

    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id)
        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_post = None
        if resource == "animals":
            new_post = method_mapper[resource]["create"](resource, post_body)
        elif resource == "locations":
            if "name" in post_body and "address" in post_body:
                self._set_headers(201)
                new_post = method_mapper[resource]["create"](resource, post_body)
            else:
                self._set_headers(400)
                new_post = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"address is required" if "address" not in post_body else ""}'
                }
        elif resource == "customers":
            new_post = method_mapper[resource]["create"](resource, post_body)
        elif resource == "employees":
            new_post = method_mapper[resource]["create"](resource, post_body)

        self.wfile.write(json.dumps(new_post).encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        if resource == "animals":
            method_mapper[resource]["update"](resource, id, post_body)
        elif resource == "locations":
            method_mapper[resource]["update"](resource, id, post_body)
        elif resource == "customers":
            method_mapper[resource]["update"](resource, id, post_body)
        elif resource == "employees":
            method_mapper[resource]["update"](resource, id, post_body)
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        (resource, id) = self.parse_url(self.path)
        if resource == "animals":
            method_mapper[resource]["delete"](resource, id)
            self._set_headers(204)
            response = {"message": "Animal deleted"}
        elif resource == "locations":
            method_mapper[resource]["delete"](resource, id)
            self._set_headers(204)
            response = {"message": "Location deleted"}
        elif resource == "customers":
            self._set_headers(405)
            response = {"message": "You can't delete a customer"}
        elif resource == "employees":
            response = {"message": "Employee deleted"}
            method_mapper[resource]["delete"](resource, id)
            self._set_headers(204)
        self.wfile.write(json.dumps(response).encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
