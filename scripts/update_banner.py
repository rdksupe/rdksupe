#!/usr/bin/env python3
"""Generate profile-banner.svg from live weather in Bokaro Steel City, India."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass

LATITUDE = 23.6693
LONGITUDE = 86.1511
OUTPUT_PATH = "assets/profile-banner.svg"

# clawd-pet (MIT) — https://github.com/abderrahimghazali/clawd-pet
CAT_UMBRELLA = """
    <rect class="umb-shadow" x="3" y="15" width="9" height="1" fill="#000" opacity="0.5"/>
    <rect class="rain1" x="-5" y="-5" width="1" height="2" fill="{rain_color}" opacity="0.5"/>
    <rect class="rain2" x="0" y="-3" width="1" height="2" fill="{rain_color}" opacity="0.5"/>
    <rect class="rain3" x="17" y="-4" width="1" height="2" fill="{rain_color}" opacity="0.5"/>
    <rect class="rain4" x="22" y="-6" width="1" height="2" fill="{rain_color}" opacity="0.5"/>
    <g class="umb-body">
      <g fill="#DE886D">
        <rect x="3" y="13" width="1" height="2"/><rect x="5" y="13" width="1" height="2"/>
        <rect x="9" y="13" width="1" height="2"/><rect x="11" y="13" width="1" height="2"/>
        <rect x="2" y="6" width="11" height="7"/>
        <rect x="0" y="9" width="2" height="2"/><rect x="13" y="7" width="2" height="2"/>
      </g>
      <rect x="14" y="7" width="1" height="8" fill="#555"/>
      <rect x="8" y="0" width="12" height="1" fill="#FF4444"/>
      <rect x="9" y="-1" width="10" height="2" fill="#FF4444"/>
      <rect x="10" y="-2" width="8" height="2" fill="#FF4444"/>
      <g class="umb-eyes" fill="#000">
        <rect x="4" y="8" width="1" height="2"/><rect x="10" y="8" width="1" height="2"/>
      </g>
    </g>"""

CAT_WAVING = """
    <rect class="wave-shadow" x="3" y="15" width="9" height="1" fill="#000" opacity="0.5"/>
    <g class="wave-body">
      <g fill="#DE886D">
        <rect x="3" y="13" width="1" height="2"/><rect x="5" y="13" width="1" height="2"/>
        <rect x="9" y="13" width="1" height="2"/><rect x="11" y="13" width="1" height="2"/>
        <rect x="2" y="6" width="11" height="7"/>
        <rect x="0" y="9" width="2" height="2"/>
        <g class="wave-arm">
          <rect x="13" y="7" width="2" height="2"/>
        </g>
      </g>
      <g class="wave-eyes" fill="#000">
        <rect x="4" y="8" width="1" height="2"/><rect x="10" y="8" width="1" height="2"/>
      </g>
    </g>"""

CAT_SLEEPING = """
    <rect x="3" y="15" width="9" height="1" fill="#000" opacity="0.35"/>
    <g fill="#DE886D">
      <rect x="3" y="13" width="1" height="2"/><rect x="5" y="13" width="1" height="2"/>
      <rect x="9" y="13" width="1" height="2"/><rect x="11" y="13" width="1" height="2"/>
      <rect x="2" y="8" width="11" height="5"/>
      <rect x="0" y="10" width="2" height="2"/><rect x="13" y="10" width="2" height="2"/>
    </g>
    <g fill="#000" opacity="0.7">
      <rect x="4" y="10" width="2" height="1"/><rect x="9" y="10" width="2" height="1"/>
    </g>
    <text x="7.5" y="6" text-anchor="middle" fill="#DE886D" font-family="monospace" font-size="3">z</text>"""


@dataclass
class Scene:
    bg: str
    rain_color: str
    rain_count: int
    rain_opacity: float
    cloud_opacity: float
    puddle_opacity: float
    show_sun: bool
    show_moon: bool
    show_stars: bool
    show_lightning: bool
    show_fog: bool
    cat_html: str
    cat_styles: str
    summary: str  # logged only, not rendered in SVG


def fetch_weather() -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}"
        "&current=temperature_2m,weather_code,is_day,relative_humidity_2m"
        "&timezone=Asia%2FKolkata"
    )
    request = urllib.request.Request(url, headers={"User-Agent": "rdksupe-profile-banner/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def weather_label(code: int) -> str:
    if code == 0:
        return "Clear"
    if code in (1, 2):
        return "Partly cloudy"
    if code == 3:
        return "Overcast"
    if code in (45, 48):
        return "Foggy"
    if code in (51, 53, 55):
        return "Drizzle"
    if code in (56, 57):
        return "Freezing drizzle"
    if code in (61, 63, 65):
        return "Rainy"
    if code in (66, 67):
        return "Freezing rain"
    if code in (71, 73, 75, 77):
        return "Snowy"
    if code in (80, 81, 82):
        return "Showers"
    if code in (85, 86):
        return "Snow showers"
    if code in (95, 96, 99):
        return "Stormy"
    return "Unknown"


def is_wet(code: int) -> bool:
    return code in {
        51, 53, 55, 56, 57, 61, 63, 65, 66, 67,
        80, 81, 82, 95, 96, 99,
    }


def is_storm(code: int) -> bool:
    return code in {95, 96, 99}


def is_foggy(code: int) -> bool:
    return code in {45, 48}


def build_scene(data: dict) -> Scene:
    current = data["current"]
    code = int(current["weather_code"])
    is_day = int(current["is_day"]) == 1
    temp = round(float(current["temperature_2m"]))
    humidity = int(current["relative_humidity_2m"])
    label = weather_label(code)
    summary = f"{temp}°C · {label} · is_day={is_day} · humidity={humidity}%"

    if is_day and code == 0:
        bg = "#2a3548"
        rain_count = 0
        cat_html = CAT_WAVING
        cat_styles = """
      .wave-body { transform-origin: 7.5px 15px; animation: wave-idle 2s infinite ease-in-out; }
      .wave-shadow { transform-origin: 7.5px 15.5px; animation: wave-shadow 2s infinite ease-in-out; }
      .wave-arm { transform-origin: 13px 9px; animation: arm-wave 0.4s infinite alternate ease-in-out; }
      .wave-eyes { transform-origin: 7.5px 8px; animation: wave-blink 3s infinite; }
      @keyframes wave-idle { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-1px); } }
      @keyframes wave-shadow { 0%, 100% { transform: scaleX(1); opacity: 0.5; } 50% { transform: scaleX(0.9); opacity: 0.4; } }
      @keyframes arm-wave { 0% { transform: rotate(-30deg); } 100% { transform: rotate(-70deg); } }
      @keyframes wave-blink { 0%, 43%, 57%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""
    elif not is_day and code == 0:
        bg = "#12121f"
        rain_count = 0
        cat_html = CAT_SLEEPING
        cat_styles = ""
    elif is_storm(code):
        bg = "#1a1a28"
        rain_count = 18
        cat_html = CAT_UMBRELLA.format(rain_color="#6a9ec7")
        cat_styles = """
      .umb-body { transform-origin: 7.5px 15px; animation: umb-sway 2s infinite ease-in-out; }
      .umb-shadow { animation: umb-s 2s infinite; }
      .umb-eyes { transform-origin: 7.5px 9px; animation: umb-blink 4s infinite; }
      @keyframes umb-sway { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-4deg); } }
      @keyframes umb-s { 0%, 100% { opacity: 0.5; } }
      @keyframes umb-blink { 0%, 46%, 54%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""
    elif is_wet(code):
        bg = "#222129"
        rain_count = 14 if code in {61, 63, 65, 80, 81, 82} else 10
        cat_html = CAT_UMBRELLA.format(rain_color="#6a9ec7")
        cat_styles = """
      .umb-body { transform-origin: 7.5px 15px; animation: umb-sway 3s infinite ease-in-out; }
      .umb-shadow { animation: umb-s 3s infinite; }
      .umb-eyes { transform-origin: 7.5px 9px; animation: umb-blink 4s infinite; }
      @keyframes umb-sway { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-2deg); } }
      @keyframes umb-s { 0%, 100% { opacity: 0.5; } }
      @keyframes umb-blink { 0%, 46%, 54%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""
    elif is_foggy(code):
        bg = "#2a2a35"
        rain_count = 4
        cat_html = CAT_UMBRELLA.format(rain_color="#8a9aa7")
        cat_styles = """
      .umb-body { transform-origin: 7.5px 15px; animation: umb-sway 4s infinite ease-in-out; }
      .umb-shadow { animation: umb-s 4s infinite; }
      .umb-eyes { transform-origin: 7.5px 9px; animation: umb-blink 5s infinite; }
      @keyframes umb-sway { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-1deg); } }
      @keyframes umb-s { 0%, 100% { opacity: 0.5; } }
      @keyframes umb-blink { 0%, 46%, 54%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""
    elif not is_day:
        bg = "#181825"
        rain_count = 6 if code >= 3 else 2
        cat_html = CAT_UMBRELLA.format(rain_color="#5a7a97")
        cat_styles = """
      .umb-body { transform-origin: 7.5px 15px; animation: umb-sway 3s infinite ease-in-out; }
      .umb-shadow { animation: umb-s 3s infinite; }
      .umb-eyes { transform-origin: 7.5px 9px; animation: umb-blink 4s infinite; }
      @keyframes umb-sway { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-2deg); } }
      @keyframes umb-s { 0%, 100% { opacity: 0.5; } }
      @keyframes umb-blink { 0%, 46%, 54%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""
    else:
        bg = "#252d3a"
        rain_count = 4 if code == 3 else 0
        cat_html = CAT_WAVING if code <= 2 else CAT_UMBRELLA.format(rain_color="#6a9ec7")
        cat_styles = """
      .wave-body { transform-origin: 7.5px 15px; animation: wave-idle 2s infinite ease-in-out; }
      .wave-shadow { transform-origin: 7.5px 15.5px; animation: wave-shadow 2s infinite ease-in-out; }
      .wave-arm { transform-origin: 13px 9px; animation: arm-wave 0.4s infinite alternate ease-in-out; }
      .wave-eyes { transform-origin: 7.5px 8px; animation: wave-blink 3s infinite; }
      @keyframes wave-idle { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-1px); } }
      @keyframes wave-shadow { 0%, 100% { transform: scaleX(1); opacity: 0.5; } 50% { transform: scaleX(0.9); opacity: 0.4; } }
      @keyframes arm-wave { 0% { transform: rotate(-30deg); } 100% { transform: rotate(-70deg); } }
      @keyframes wave-blink { 0%, 43%, 57%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }
      .umb-body { transform-origin: 7.5px 15px; animation: umb-sway 3s infinite ease-in-out; }
      .umb-shadow { animation: umb-s 3s infinite; }
      .umb-eyes { transform-origin: 7.5px 9px; animation: umb-blink 4s infinite; }
      @keyframes umb-sway { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-2deg); } }
      @keyframes umb-s { 0%, 100% { opacity: 0.5; } }
      @keyframes umb-blink { 0%, 46%, 54%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.1); } }"""

    return Scene(
        bg=bg,
        rain_color="#6a9ec7" if is_day else "#5a7a97",
        rain_count=rain_count,
        rain_opacity=0.55 if is_storm(code) else 0.45,
        cloud_opacity=0.65 if code >= 3 or is_foggy(code) else 0.45,
        puddle_opacity=0.14 if is_wet(code) else 0.08,
        show_sun=is_day and code == 0,
        show_moon=not is_day and code <= 2,
        show_stars=not is_day and code <= 3,
        show_lightning=is_storm(code),
        show_fog=is_foggy(code),
        cat_html=cat_html,
        cat_styles=cat_styles,
        summary=summary,
    )


def rain_styles(max_drops: int) -> str:
    lines = [
        "      @keyframes rain-fall { 0% { transform: translateY(-15px); opacity: 0.6; } 100% { transform: translateY(20px); opacity: 0; } }",
        "      .bubble { animation: bubble-pulse 2s infinite ease-in-out; }",
        "      @keyframes bubble-pulse { 0%, 100% { opacity: 0.75; } 50% { opacity: 1; } }",
    ]
    for index in range(1, max(max_drops, 1) + 1):
        delay = (index * 0.11) % 0.9
        duration = 0.55 + (index % 5) * 0.12
        lines.append(
            f"      .rain{index} {{ animation: rain-fall {duration:.2f}s infinite linear {delay:.2f}s; }}"
        )
    if max_drops == 0:
        lines.append("      .rain1 { animation: none; }")
    return "\n".join(lines)


def rain_markup(count: int, color: str, opacity: float) -> str:
    if count == 0:
        return ""
    drops = []
    for index in range(count):
        x = 20 + (index * 31) % 520
        y = 14 + (index * 7) % 18
        cls = f"rain{(index % 12) + 1}"
        drops.append(
            f'  <rect class="{cls}" x="{x}" y="{y}" width="1.5" height="4" '
            f'fill="{color}" opacity="{opacity}"/>'
        )
    return "\n".join(drops)


def stars_markup() -> str:
    parts = []
    coords = [(40, 22), (120, 14), (200, 28), (320, 18), (420, 24), (500, 12), (80, 36), (460, 34)]
    for x, y in coords:
        parts.append(f'  <circle cx="{x}" cy="{y}" r="1" fill="#fff" opacity="0.55"/>')
    return "\n".join(parts)


def render(scene: Scene) -> str:
    max_rain_class = max(scene.rain_count, 12)
    lightning = ""
    if scene.show_lightning:
        lightning = """
      .lightning { animation: lightning-flash 5s infinite; }
      @keyframes lightning-flash {
        0%, 89%, 100% { opacity: 0; }
        90%, 91% { opacity: 0.18; }
        92% { opacity: 0; }
        93%, 94% { opacity: 0.12; }
      }"""

    sun = ""
    if scene.show_sun:
        sun = """
  <circle cx="480" cy="32" r="16" fill="#FFD166" opacity="0.9"/>
  <circle cx="480" cy="32" r="22" fill="#FFD166" opacity="0.15"/>"""

    moon = ""
    if scene.show_moon:
        moon = """
  <circle cx="470" cy="30" r="12" fill="#E8E8F0" opacity="0.85"/>
  <circle cx="476" cy="27" r="10" fill="{bg}" opacity="1"/>""".format(bg=scene.bg)

    fog = ""
    if scene.show_fog:
        fog = """
  <rect x="0" y="50" width="560" height="70" fill="#9aa0ad" opacity="0.08"/>
  <rect x="0" y="70" width="560" height="50" fill="#9aa0ad" opacity="0.06"/>"""

    stars = stars_markup() if scene.show_stars else ""
    rain = rain_markup(scene.rain_count, scene.rain_color, scene.rain_opacity)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 160" width="560" height="160">
  <!-- Auto-generated for Bokaro Steel City · scripts/update_banner.py -->
  <defs>
    <style>
{scene.cat_styles}
{rain_styles(max_rain_class)}
{lightning}
    </style>
  </defs>

  <rect x="0" y="0" width="560" height="160" rx="8" fill="{scene.bg}"/>
  <rect class="lightning" x="0" y="0" width="560" height="160" rx="8" fill="#fff" opacity="0"/>

  <ellipse cx="60" cy="26" rx="50" ry="14" fill="#3a3945" opacity="{scene.cloud_opacity}"/>
  <ellipse cx="500" cy="28" rx="48" ry="13" fill="#3a3945" opacity="{scene.cloud_opacity}"/>
  <ellipse cx="280" cy="20" rx="70" ry="16" fill="#3a3945" opacity="{scene.cloud_opacity * 0.7:.2f}"/>
{sun}{moon}{stars}{fog}
{rain}
  <ellipse cx="280" cy="148" rx="170" ry="7" fill="{scene.rain_color}" opacity="{scene.puddle_opacity}"/>

  <g transform="translate(242, 68) scale(5)">
{scene.cat_html}
  </g>

  <g class="bubble">
    <rect x="350" y="36" width="86" height="34" rx="11" fill="{scene.bg}" stroke="#DE886D" stroke-width="1.5"/>
    <polygon points="352,64 360,64 346,76" fill="{scene.bg}" stroke="#DE886D" stroke-width="1"/>
    <text x="393" y="59" text-anchor="middle" fill="#DE886D" font-family="monospace" font-size="14" font-weight="bold">meow~!</text>
  </g>
</svg>
"""


def main() -> int:
    try:
        data = fetch_weather()
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"Failed to fetch weather: {error}", file=sys.stderr)
        return 1

    scene = build_scene(data)
    svg = render(scene)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(svg)
        handle.write("\n")

    print(f"Wrote {OUTPUT_PATH}")
    print(f"  Scene: {scene.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
