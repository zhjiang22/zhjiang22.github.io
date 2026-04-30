"""Fetch Google Scholar citation stats and write to _data/scholar.yml."""
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "6F85yPcAAAAJ")
OUTPUT = Path(__file__).resolve().parent.parent / "_data" / "scholar.yml"
TIMEOUT_SECONDS = int(os.environ.get("SCHOLAR_FETCH_TIMEOUT", "30"))
MAX_ATTEMPTS = int(os.environ.get("SCHOLAR_FETCH_ATTEMPTS", "3"))
RETRY_DELAY_SECONDS = float(os.environ.get("SCHOLAR_FETCH_RETRY_DELAY", "5"))
ALLOW_STALE_ON_FAILURE = (
    os.environ.get("ALLOW_STALE_ON_FAILURE", "").strip().lower()
    in {"1", "true", "yes", "on"}
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

METRIC_KEYS = (
    "citations_all",
    "citations_5y",
    "h_index_all",
    "h_index_5y",
    "i10_index_all",
    "i10_index_5y",
)


def load_existing_stats():
    if not OUTPUT.exists():
        return {}

    stats = {}
    for line in OUTPUT.read_text().splitlines():
        if ":" not in line or line.startswith("#"):
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip().strip('"')
        if key not in METRIC_KEYS:
            continue
        try:
            stats[key] = int(raw_value)
        except ValueError:
            continue
    return stats


def parse_stats_table(soup):
    cells = soup.select("td.gsc_rsb_std")
    if len(cells) < 5:
        return None

    values = []
    for cell in cells[:6]:
        raw_value = cell.get_text(strip=True).replace(",", "")
        if not raw_value.isdigit():
            return None
        values.append(int(raw_value))

    return {
        "citations_all": values[0],
        "citations_5y": values[1],
        "h_index_all": values[2],
        "h_index_5y": values[3],
        "i10_index_all": values[4],
        "i10_index_5y": values[5] if len(values) > 5 else 0,
    }


def parse_citation_count_from_meta(soup):
    candidates = []
    for attrs in (
        {"name": "description"},
        {"property": "og:description"},
    ):
        tag = soup.find("meta", attrs=attrs)
        if tag and tag.get("content"):
            candidates.append(tag["content"])

    for content in candidates:
        match = re.search(r"\bCited by\s+([\d,]+)\b", content, flags=re.IGNORECASE)
        if match:
            return int(match.group(1).replace(",", ""))
    return None


def parse_stats(html):
    soup = BeautifulSoup(html, "html.parser")

    table_stats = parse_stats_table(soup)
    if table_stats:
        return table_stats

    citation_count = parse_citation_count_from_meta(soup)
    if citation_count is not None:
        existing_stats = load_existing_stats()
        if existing_stats:
            fallback_stats = {
                key: existing_stats.get(key, 0) for key in METRIC_KEYS
            }
            previous_all = fallback_stats.get("citations_all")
            previous_5y = fallback_stats.get("citations_5y")
            fallback_stats["citations_all"] = citation_count
            if previous_all == previous_5y:
                fallback_stats["citations_5y"] = citation_count
            print(
                "Falling back to meta description for citation count; "
                "keeping previous values for unavailable metrics.",
                file=sys.stderr,
            )
            return fallback_stats

    title = soup.title.get_text(strip=True) if soup.title else "<no title>"
    raise ValueError(
        "Unexpected page structure, found no usable Google Scholar metrics "
        f"(title={title})"
    )


def fetch_stats():
    url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT_SECONDS)
            try:
                return parse_stats(resp.text)
            except ValueError as parse_exc:
                if resp.status_code >= 400:
                    raise requests.HTTPError(
                        f"{resp.status_code} response with no usable metrics "
                        f"from {url}"
                    ) from parse_exc
                raise
        except (requests.RequestException, ValueError) as exc:
            last_error = exc
            print(
                f"Attempt {attempt}/{MAX_ATTEMPTS} failed while fetching "
                f"Google Scholar stats: {exc}",
                file=sys.stderr,
            )
            if attempt < MAX_ATTEMPTS:
                time.sleep(RETRY_DELAY_SECONDS * attempt)

    raise RuntimeError(
        f"Failed to fetch Google Scholar stats after {MAX_ATTEMPTS} attempts"
    ) from last_error


def write_yaml(stats):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Auto-generated by fetch_scholar.py - do not edit manually",
        f"updated: \"{now}\"",
        f"scholar_id: \"{SCHOLAR_ID}\"",
    ]
    for key, val in stats.items():
        lines.append(f"{key}: {val}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUTPUT}")
    for key, val in stats.items():
        print(f"  {key}: {val}")


if __name__ == "__main__":
    try:
        stats = fetch_stats()
    except Exception as exc:  # noqa: BLE001 - surface a clear workflow message
        if ALLOW_STALE_ON_FAILURE and OUTPUT.exists():
            print(
                "::warning::Failed to refresh Google Scholar stats; "
                f"keeping the existing {OUTPUT.name}. Reason: {exc}",
                file=sys.stderr,
            )
            sys.exit(0)

        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    write_yaml(stats)
