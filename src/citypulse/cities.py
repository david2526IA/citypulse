from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class City:
    name: str
    latitude: float
    longitude: float
    timezone: str


CITIES = {
    "barcelona": City("Barcelona", 41.3874, 2.1686, "Europe/Madrid"),
    "bilbao": City("Bilbao", 43.2630, -2.9350, "Europe/Madrid"),
    "madrid": City("Madrid", 40.4168, -3.7038, "Europe/Madrid"),
    "seville": City("Seville", 37.3891, -5.9845, "Europe/Madrid"),
    "valencia": City("Valencia", 39.4699, -0.3763, "Europe/Madrid"),
}


def get_city(name: str) -> City:
    city = CITIES.get(name.lower())
    if not city:
        raise ValueError(f"Unknown city '{name}'. Choose from: {', '.join(sorted(CITIES))}")
    return city
