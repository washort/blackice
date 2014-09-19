from rest_framework.exceptions import APIException


class HttpLegallyUnavailable(APIException):
    status_code = 451
    default_detail = 'Legally unavailable.'

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail
