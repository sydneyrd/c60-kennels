import json
from repository import all, single, create, delete, update
from http.server import BaseHTTPRequestHandler, HTTPServer
# from views import (get_all_animals, get_single_animal, update_customer, update_employee, update_location, update_animal, get_single_location, delete_location, delete_animal, delete_customer, delete_employee, get_all_locations, get_all_employees, delete_animal, get_single_employee,
# get_all_customers, get_single_customer, create_animal, create_location, create_customer, create_employee)

method_mapper = {

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
  

    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id)
        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
     

        self.wfile.write(json.dumps(new_post).encode())

    def do_PUT(self):
   

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



def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
