from app.internal.cities.domain.interfaces.city import ICityRepository


class CityService:
    def __init__(self, city_repo: ICityRepository) -> None:
        self.city_repo = city_repo

    def get_cities_list(self, request):
        return self.city_repo.get_cities_list()

    def is_city_valid(self, city: str) -> bool:
        return self.city_repo.is_city_valid(city)
