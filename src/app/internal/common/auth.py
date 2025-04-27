from ninja.security import HttpBearer


class HTTPJWTAuth(HttpBearer):
    def authenticate(self, request, token):
        request.user_id = 1
        return token
