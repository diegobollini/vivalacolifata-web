#!/usr/bin/env python3
"""Check that every page uses the live stream and that it returns audio."""

from pathlib import Path
from urllib.request import Request, urlopen


STREAM_URL = "https://radios.solumedia.com/6076/stream?icy=http"
ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "index.html", ROOT / "en/index.html", ROOT / "fr/index.html")


def main() -> None:
    for page in PAGES:
        occurrences = page.read_text(encoding="utf-8").count(STREAM_URL)
        if occurrences != 1:
            raise SystemExit(
                f"{page.relative_to(ROOT)}: expected one stream reference, "
                f"found {occurrences}"
            )

    request = Request(STREAM_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=15) as response:
        content_type = response.headers.get_content_type()
        station = response.headers.get("icy-name", "")
        sample = response.read(4096)

    if not content_type.startswith("audio/"):
        raise SystemExit(f"unexpected stream content type: {content_type}")
    if station != "Radio La Colifata":
        raise SystemExit(f"unexpected station name: {station or 'missing'}")
    if not sample:
        raise SystemExit("stream returned no audio data")

    print(f"Stream OK: {station} ({content_type})")


if __name__ == "__main__":
    main()
