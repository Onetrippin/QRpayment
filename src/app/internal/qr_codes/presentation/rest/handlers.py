from app.internal.qr_codes.domain.services.qr_code import QRcodeService


class QRcodeHandlers:
    def __init__(self, qr_code_service: QRcodeService) -> None:
        self.qr_code_service = qr_code_service
