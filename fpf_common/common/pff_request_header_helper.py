from flask import request
import re


class PFFRequestHeaderHelper:

    def get_header(self, name: str, default=None):
        return request.headers.get(name, default)

    def get_authorization_header(self):
        header = self.get_header("Authorization")
        if not header:
            header = self.get_header("authorization")
        return header

    def get_bearer_token(self):
        authorization_header = self.get_authorization_header()
        if not authorization_header:
            return None
        group = re.match("^Bearer\\s+(.*)", authorization_header)
        if group:
            return group.group(1)
        return None

    def get_url_info(self):
        url_dictionary = {}
        if request and request.url:
            url_dictionary['relative_url'] = str(request.url_rule)
            url_dictionary['relative_url_with_param'] = str(request.full_path)
            url_dictionary['host_with_port'] = str(request.host)
            url_dictionary['method'] = str(request.method)
            url_dictionary['charset'] = str(request.url_charset)
        return url_dictionary


pff_request_header_helper = PFFRequestHeaderHelper()
