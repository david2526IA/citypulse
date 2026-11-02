from __future__ import annotations

import argparse
import json

from .cities import CITIES
from .service import snapshot


def main() -> None:
    parser = argparse.ArgumentParser(prog="citypulse")
    parser.add_argument("city", choices=sorted(CITIES), nargs="?", default="madrid")
    parser.add_argument("--cache", default="citypulse-cache.json")
    args = parser.parse_args()
    from .cache import JsonCache
    print(json.dumps(snapshot(args.city, JsonCache(args.cache)), indent=2))


if __name__ == "__main__":
    main()
