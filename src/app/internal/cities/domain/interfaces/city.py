from abc import ABC, abstractmethod
from typing import List

from app.internal.cities.domain.entities.city import CitySchema


class ICityRepository(ABC):
    @abstractmethod
    def get_cities_list(self) -> List[CitySchema]:
        ...
