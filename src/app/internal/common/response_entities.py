from ninja import Schema


class SuccessResponse(Schema):
    success: str


class ErrorResponse(Schema):
    error: str
