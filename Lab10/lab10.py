import pytest


class BadHTTPVersion(Exception):
    pass


class BadRequestTypeError(Exception):
    pass


class http_req:

    def __init__(self, request):
        request = request.split(" ")

        self.type = request[0]
        self.path = request[1]
        self.protocol = request[2]


def reqstr2obj(request_string):
    if isinstance(request_string, str) is False:
        raise TypeError
    if len(request_string.strip().split(" ")) != 3:
        return None

    httpResult = http_req(request_string)

    if httpResult.protocol not in ['HTTP1.0', 'HTTP1.1', 'HTTP2.0']:
        raise BadHTTPVersion

    if httpResult.path.startswith('/') == False:
        raise ValueError("Resource path does not start with /")

    if httpResult.type not in ['GET', 'PUT', 'DELETE', 'TRACE', 'OPTIONS', 'PATCH', 'POST', 'CONNECT', 'HEAD']:
        raise BadRequestTypeError

    return httpResult


def test_1():
    with pytest.raises(TypeError):
        reqstr2obj(123)


def test_2():
    assert isinstance(reqstr2obj("GET / HTTP1.1"), http_req)


def test_3():
    testhttp = reqstr2obj("GET / HTTP1.1")

    assert testhttp.protocol == "HTTP1.1"
    assert testhttp.type == "GET"
    assert testhttp.path == "/"


def test_4():
    args = "POST /index HTTP1.1"
    testHttp = reqstr2obj(args)

    argsplit = args.split(" ")
    assert testHttp.path == argsplit[1]
    assert testHttp.protocol == argsplit[2]
    assert testHttp.type == argsplit[0]


def test_5():
    assert reqstr2obj("GET GET / HTTP1.1") == None
    assert reqstr2obj("POST / GET HTTP2.0") == None
    assert reqstr2obj("POST HTTP1.1") == None
    assert reqstr2obj("HTTP1.1") == None
    assert reqstr2obj(" ") == None
    assert reqstr2obj("") == None


def test_6():
    with pytest.raises(BadRequestTypeError):
        reqstr2obj("DOWNLOAD /movie.mp4 HTTP1.1")


def test_7():
    with pytest.raises(BadHTTPVersion):
        reqstr2obj("GET /movie.mp4 HTTP10")
    with pytest.raises(BadHTTPVersion):
        reqstr2obj("GET /movie.mp4 HTTP0")
    with pytest.raises(BadHTTPVersion):
        reqstr2obj("GET /movie.mp4 HTTP5")


def test_8():
    with pytest.raises(ValueError) as testException :

        reqstr2obj("DOWNLOAD movie.mp4 HTTP1.0")

    assert "Resource path does not start with /" in str(testException)


def run():
    print("Test it with Pytest Framework")


if __name__ == "__main__":
    run()
