#!/usr/bin/env python3
"""Insert a random xkcd comic into README.md between marker comments."""

from __future__ import annotations

import json
import random
import re
import sys
import urllib.error
import urllib.request

README_PATH = "README.md"
START_MARKER = "<!-- xkcd:start -->"
END_MARKER = "<!-- xkcd:end -->"
COMIC_WIDTH = 400


def fetch_random_comic() -> dict:
    request = urllib.request.Request(
        "https://xkcd.com/info.0.json",
        headers={"User-Agent": "rdksupe-profile-xkcd/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        latest = json.load(response)

    number = random.randint(1, int(latest["num"]))
    if number == int(latest["num"]):
        return latest

    request = urllib.request.Request(
        f"https://xkcd.com/{number}/info.0.json",
        headers={"User-Agent": "rdksupe-profile-xkcd/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def render_block(comic: dict) -> str:
    title = comic["safe_title"]
    number = comic["num"]
    alt = re.sub(r"\s+", " ", comic["alt"]).strip()
    image = comic["img"]
    link = comic.get("url") or f"https://xkcd.com/{number}/"

    return f"""[![{title}]({image})]({link})

*{alt}*"""


def update_readme(block: str) -> None:
    with open(README_PATH, encoding="utf-8") as handle:
        contents = handle.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(contents):
        raise SystemExit(f"Markers {START_MARKER} / {END_MARKER} not found in {README_PATH}")

    replacement = f"{START_MARKER}\n\n{block}\n\n{END_MARKER}"
    updated = pattern.sub(replacement, contents, count=1)

    with open(README_PATH, "w", encoding="utf-8") as handle:
        handle.write(updated)


def main() -> int:
    try:
        comic = fetch_random_comic()
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError) as error:
        print(f"Failed to fetch xkcd: {error}", file=sys.stderr)
        return 1

    block = render_block(comic)
    update_readme(block)
    print(f"Updated {README_PATH} with xkcd #{comic['num']}: {comic['safe_title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
