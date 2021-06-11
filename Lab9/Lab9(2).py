import pytest
import lab9 as app10
from main import MyHttpRequest, BadRequestTypeError, BadHTTPVersion


class TestLab10:
    def test_1(self):
        with pytest.raises(TypeError):
            app10.reqstr2obj(123)

        with pytest.raises(TypeError):
            app10.reqstr2obj([])

    def test_2(self):
        instance = app10.reqstr2obj("GET / HTTP1.1")

        assert type(instance) == MyHttpRequest

    def test_3(self):
        instance = app10.reqstr2obj("GET / HTTP1.1")

        assert instance.request_type == "GET"
        assert instance.resource_path == "/"
        assert instance.protocol_type == "HTTP1.1"

    @pytest.mark.parametrize("request_type, resource_path, protocol_type",
                             [("POST", "/accounts", "HTTP1.1"), ("PATCH", "/profiles/5", "HTTP1.1")])
    def test_4(self, request_type, resource_path, protocol_type):
        instance = app10.reqstr2obj(f"{request_type} {resource_path} {protocol_type}")

        assert instance.request_type == request_type
        assert instance.resource_path == resource_path
        assert instance.protocol_type == protocol_type

    @pytest.mark.parametrize("request_str",
                             ["GET /", "POST HTTP1.1", "", "  ", "GET  /    HTTP1.1"])
    def test_5(self, request_str):
        instance = app10.reqstr2obj(request_str)

        assert instance is None

    @pytest.mark.parametrize("request_str",
                             ["DOWNLOAD /photo HTTP1.1", "UPLOAD /files HTTP1.1"])
    def test_6(self, request_str):
        with pytest.raises(BadRequestTypeError):
            app10.reqstr2obj(request_str)

    @pytest.mark.parametrize("request_str",
                             ["GET /photo/4514 HTTP1.5", "POST /files HTTP3.0", "POST /files HTTP"])
    def test_7(self, request_str):
        with pytest.raises(BadHTTPVersion):
            app10.reqstr2obj(request_str)

    @pytest.mark.parametrize("request_str",
                             ["GET photo/4514 HTTP1.1", "POST files HTTP1.1", "POST downloads HTTP1.1"])
    def test_8(self, request_str):
        with pytest.raises(ValueError):
            app10.reqstr2obj(request_str)
