class BadRequestTypeError(Exception):
    pass


class BadHTTPVersion(Exception):
    pass


class MyHttpRequest:
    def __init__(self, request_type, resource_path, protocol_type):
        self.request_type = request_type
        self.resource_path = resource_path
        self.protocol_type = protocol_type


def reqstr2obj(request_string):
    if type(request_string) == str:
        request_data = request_string.strip().split(" ")

        if len(request_data) != 3:
            return None

        request_type = request_data[0]
        resource_path = request_data[1]
        protocol_type = request_data[2]

        if request_type not in ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]:
            raise BadRequestTypeError

        if protocol_type not in ["HTTP1.0", "HTTP1.1", "HTTP2.0"]:
            raise BadHTTPVersion

        if resource_path[0] != "/":
            raise ValueError("Resource path must begin with a slash (\"/\")")

        return MyHttpRequest(request_type, resource_path, protocol_type)
    else:
        raise TypeError("Request string has to be of type string.")