from ninja import Schema


class SuccessResponse(Schema):
    success: bool


class ErrorResponse(Schema):
    error: str
