# CityPulse

> A local-first city conditions app using public weather and air-quality data.

[![CI](https://github.com/david2526IA/citypulse/actions/workflows/ci.yml/badge.svg)](https://github.com/david2526IA/citypulse/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Open-Meteo](https://img.shields.io/badge/Data-Open--Meteo-0EA5E9)](https://open-meteo.com/)

CityPulse provides a quick, understandable snapshot of current weather and air-quality conditions for selected Spanish cities. It uses keyless public endpoints, caches results locally for 15 minutes and exposes the same data through a CLI, a FastAPI endpoint and a lightweight web interface.

## Features

- Current temperature, apparent temperature, rain and wind.
- European AQI, PM2.5, PM10, ozone and nitrogen dioxide where reported.
- Local JSON cache to reduce repeated external calls.
- Five supported cities: Madrid, Barcelona, Bilbao, Seville and Valencia.
- No account or API key required.
- CLI, web UI, Docker, tests and CI.

## Quick start

```bash
git clone https://github.com/david2526IA/citypulse.git
cd citypulse
python -m venv .venv
```

Activate the environment, then:

```bash
pip install -e ".[dev]"
citypulse madrid
pytest -q
```

## Local web app

```bash
pip install -e ".[web]"
uvicorn citypulse.api:app --reload
```

Open `http://127.0.0.1:8000`. The API is also available at `/v1/snapshot/{city}`.

```bash
docker build -t citypulse .
docker run --rm -p 8000:8000 citypulse
```

## Data source and limitations

Weather and air-quality data are requested from [Open-Meteo](https://open-meteo.com/). CityPulse is a planning aid, not an official warning service or medical tool. Check official local alerts and appropriate health guidance, especially when air-quality conditions are poor.

## Roadmap

- [ ] City search through geocoding
- [ ] Historical trends and visual charts
- [ ] Official alert-provider adapters
- [ ] PWA/offline shell
- [ ] Accessibility audit

## License

MIT © 2026 David
