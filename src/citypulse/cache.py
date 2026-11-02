from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


class JsonCache:
    def __init__(self, path: str | Path = "citypulse-cache.json", max_age_minutes: int = 15) -> None:
        self.path = Path(path)
        self.max_age = timedelta(minutes=max_age_minutes)

    def get(self, key: str) -> dict[str, object] | None:
        if not self.path.exists():
            return None
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        item = payload.get(key)
        if not item:
            return None
        cached_at = datetime.fromisoformat(item["cached_at"])
        if datetime.now(timezone.utc) - cached_at > self.max_age:
            return None
        return item["value"]

    def set(self, key: str, value: dict[str, object]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {}
        payload[key] = {"cached_at": datetime.now(timezone.utc).isoformat(), "value": value}
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
