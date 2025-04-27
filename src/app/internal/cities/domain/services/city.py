from app.internal.cities.domain.interfaces.city import ICityRepository


class CityService:
    def __init__(self, city_repo: ICityRepository) -> None:
        self.city_repo = city_repo
