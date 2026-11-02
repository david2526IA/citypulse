"""Minimal client for Open-Meteo's keyless public forecast endpoints."""

from __future__ import annotations

import json
from urllib.parse import urlencode
from urllib.request import urlopen

from .cities import City


def _get_json(base: str, parameters: dict[str, object]) -> dict[str, object]:
    url = f"{base}?{urlencode(parameters)}"
    with urlopen(url, timeout=12) as response:  # nosec B310: fixed HTTPS API origin
        return json.loads(response.read().decode("utf-8"))


def fetch_current(city: City) -> dict[str, object]:
    common = {"latitude": city.latitude, "longitude": city.longitude, "timezone": city.timezone}
    weather = _get_json("https://api.open-meteo.com/v1/forecast", {
        **common, "current": "temperature_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code",
    })
    air = _get_json("https://air-quality-api.open-meteo.com/v1/air-quality", {
        **common, "current": "european_aqi,pm2_5,pm10,nitrogen_dioxide,ozone",
    })
    return {"weather": weather["current"], "air": air["current"]}
