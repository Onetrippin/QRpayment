from app.internal.cities.domain.services.city import CityService


class CityHandlers:
    def __init__(self, city_service: CityService) -> None:
        self.city_service = city_service
