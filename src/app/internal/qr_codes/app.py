from ninja import NinjaAPI

from app.internal.qr_codes.data.repositories.qr_code import QRcodeRepository
from app.internal.qr_codes.domain.services.qr_code import QRcodeService
from app.internal.qr_codes.presentation.rest.handlers import QRcodeHandlers
from app.internal.qr_codes.presentation.rest.routers import get_qr_codes_router


def add_qrcodes_router(api: NinjaAPI, path: str) -> None:
    qr_code_repo = QRcodeRepository()
    qr_code_service = QRcodeService(qr_code_repo=qr_code_repo)
    qr_code_handlers = QRcodeHandlers(qr_code_service=qr_code_service)

    qr_codes_router = get_qr_codes_router(qr_code_handlers)
    api.add_router(path, qr_codes_router)
