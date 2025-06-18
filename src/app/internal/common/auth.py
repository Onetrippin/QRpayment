import uuid

from ninja.security import HttpBearer


class HTTPJWTAuth(HttpBearer):
    def authenticate(self, request, token):
        request.user_id = 1
        request.user_uuid = uuid.uuid4()
        return token
