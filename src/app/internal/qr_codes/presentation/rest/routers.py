from ninja import Router

from app.internal.qr_codes.presentation.rest.handlers import QRcodeHandlers


def get_qr_codes_router(qr_code_handlers: QRcodeHandlers) -> Router:
    router = Router(tags=['QRcodes'])

    return router
