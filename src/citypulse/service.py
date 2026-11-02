from __future__ import annotations

from typing import Callable

from .cache import JsonCache
from .cities import get_city
from .client import fetch_current


def _air_label(aqi: float | int | None) -> str:
    if aqi is None:
        return "unavailable"
    if aqi <= 20:
        return "good"
    if aqi <= 40:
        return "fair"
    if aqi <= 60:
        return "moderate"
    if aqi <= 80:
        return "poor"
    return "very poor"


def snapshot(name: str, cache: JsonCache | None = None, fetcher: Callable = fetch_current) -> dict[str, object]:
    city = get_city(name)
    cache = cache or JsonCache()
    key = city.name.lower()
    cached = cache.get(key)
    if cached:
        return {**cached, "cache": "hit"}
    raw = fetcher(city)
    weather = raw["weather"]
    air = raw["air"]
    aqi = air.get("european_aqi")
    result = {
        "city": city.name,
        "observed_at": weather.get("time"),
        "weather": {
            "temperature_c": weather.get("temperature_2m"), "apparent_temperature_c": weather.get("apparent_temperature"),
            "precipitation_mm": weather.get("precipitation"), "wind_kmh": weather.get("wind_speed_10m"),
        },
        "air_quality": {"european_aqi": aqi, "label": _air_label(aqi), "pm2_5": air.get("pm2_5"), "pm10": air.get("pm10"), "ozone": air.get("ozone")},
        "notice": "Snapshot for planning only. Check official local alerts and health guidance when conditions are poor.",
    }
    cache.set(key, result)
    return {**result, "cache": "miss"}
