from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from .cities import CITIES
from .service import snapshot

app = FastAPI(title="CityPulse API", version="0.1.0")


@app.get("/")
def home() -> FileResponse:
    return FileResponse(Path(__file__).parent / "web" / "index.html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/cities")
def cities() -> list[str]:
    return sorted(CITIES)


@app.get("/v1/snapshot/{city}")
def current(city: str) -> dict[str, object]:
    try:
        return snapshot(city)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
