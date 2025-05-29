from app.internal.qr_codes.domain.interfaces.qr_code import IQRcodeRepository


class QRcodeService:
    def __init__(self, qr_code_repo: IQRcodeRepository) -> None:
        self.qr_code_repo = qr_code_repo
