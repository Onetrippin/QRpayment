from typing import List

from app.internal.cities.data.models.city import City
from app.internal.cities.domain.entities.city import CitySchema
from app.internal.cities.domain.interfaces.city import ICityRepository


class CityRepository(ICityRepository):
    def get_cities_list(self) -> List[CitySchema]:
        cities = City.objects.all().values('id', 'name', 'is_active')

        return [CitySchema(**city) for city in cities]

    def is_city_valid(self, city: str) -> bool:
        return City.objects.filter(name__iexact=city, is_active=True).exists()
