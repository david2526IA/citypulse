from citypulse.cache import JsonCache
from citypulse.service import snapshot


def fake_fetcher(_city):
    return {"weather": {"time": "2026-01-01T12:00", "temperature_2m": 18.0, "apparent_temperature": 17.2, "precipitation": 0.0, "wind_speed_10m": 9.0}, "air": {"european_aqi": 31, "pm2_5": 8, "pm10": 12, "ozone": 65}}


def test_snapshot_normalises_public_data_and_caches(tmp_path) -> None:
    cache = JsonCache(tmp_path / "nested" / "cache.json")
    result = snapshot("madrid", cache=cache, fetcher=fake_fetcher)
    assert result["city"] == "Madrid"
    assert result["air_quality"]["label"] == "fair"
    assert result["cache"] == "miss"
    cached = snapshot("madrid", cache=cache, fetcher=lambda _: (_ for _ in ()).throw(AssertionError()))
    assert cached["cache"] == "hit"


def test_unknown_city_is_rejected() -> None:
    try:
        snapshot("unknown", fetcher=fake_fetcher)
    except ValueError as error:
        assert "Unknown city" in str(error)
    else:
        raise AssertionError("Expected unknown city to fail")
