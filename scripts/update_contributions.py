"""Render the latest 31 days of the public GitHub contribution calendar as SVG."""

from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.request import Request, urlopen


CALENDAR_URL = "https://github.com/users/Shan-yan/contributions"
CHART_PATH = Path(__file__).resolve().parents[1] / "assets" / "contributions.svg"
DAYS = 31
COUNT = re.compile(r"^(No|[\d,]+)\s+contributions?\b")


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.counts = {}
        self.tooltip_id = None
        self.tooltip_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and {"id", "data-date"} <= attrs.keys():
            self.dates[attrs["id"]] = date.fromisoformat(attrs["data-date"])
        elif tag == "tool-tip":
            self.tooltip_id = attrs.get("for")
            self.tooltip_text = []

    def handle_data(self, data):
        if self.tooltip_id:
            self.tooltip_text.append(data)

    def handle_endtag(self, tag):
        if tag == "tool-tip" and self.tooltip_id:
            match = COUNT.match("".join(self.tooltip_text).strip())
            if match:
                value = match[1]
                self.counts[self.tooltip_id] = 0 if value == "No" else int(value.replace(",", ""))
            self.tooltip_id = None


def recent_contributions(html):
    calendar = CalendarParser()
    calendar.feed(html)
    dates = sorted(calendar.dates.items(), key=lambda item: item[1])[-DAYS:]
    if (
        len(dates) != DAYS
        or any(current - previous != timedelta(days=1) for (_, previous), (_, current) in zip(dates, dates[1:]))
        or any(cell not in calendar.counts for cell, _ in dates)
    ):
        raise ValueError("GitHub did not return 31 consecutive days with contribution counts.")
    return [(day, calendar.counts[cell]) for cell, day in dates]


def render_chart(days):
    width, height = 800, 258
    left, right, top, bottom = 48, 774, 76, 212
    step = max(1, (max(count for _, count in days) + 3) // 4)
    upper = step * 4
    start, end = days[0][0], days[-1][0]

    def x(index):
        return left + (right - left) * index / (len(days) - 1)

    def y(count):
        return bottom - (bottom - top) * count / upper

    grid = "\n".join(
        f'  <path class="grid" d="M{left} {y(tick):.1f}H{right}"/>'
        f'<text x="{left - 10}" y="{y(tick) + 5:.1f}" text-anchor="end">{tick}</text>'
        for tick in range(0, upper + 1, step)
    )
    labels = "\n".join(
        f'  <text x="{x(index):.1f}" y="237" text-anchor="{anchor}">{days[index][0]:%m-%d}</text>'
        for index, anchor in [(0, "start"), (7, "middle"), (14, "middle"), (21, "middle"), (30, "end")]
    )
    points = " ".join(f"{x(index):.1f},{y(count):.1f}" for index, (_, count) in enumerate(days))
    last_y = y(days[-1][1])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">GitHub contributions per day</title>
  <desc id="desc">Shan-yan, {start} through {end}. Daily values are available in the GitHub contribution calendar.</desc>
  <style>
    text {{ fill: #4b5563; font: 15px system-ui, sans-serif; }}
    .card {{ fill: #f7f8ff; stroke: #dedff1; }}
    .heading {{ fill: #222643; font-size: 20px; font-weight: 700; }}
    .grid {{ stroke: #dde0f0; }}
    .line {{ stroke: #6250d6; }}
    .point {{ fill: #6250d6; stroke: #f7f8ff; }}
    @media (prefers-color-scheme: dark) {{
      text {{ fill: #bdc8dd; }}
      .card {{ fill: #11182d; stroke: #303856; }}
      .heading {{ fill: #f0efff; }}
      .grid {{ stroke: #2d354f; }}
      .line {{ stroke: #9085e9; }}
      .point {{ fill: #9085e9; stroke: #11182d; }}
    }}
  </style>
  <rect class="card" x=".5" y=".5" width="799" height="257" rx="16"/>
  <text class="heading" x="{left}" y="33">GitHub contributions / day</text>
  <text x="{left}" y="55">{start} – {end}</text>
{grid}
{labels}
  <polyline class="line" points="{points}" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle class="point" cx="{right}" cy="{last_y:.1f}" r="5" stroke-width="2"/>
</svg>
'''


def main():
    request = Request(CALENDAR_URL, headers={"Accept-Language": "en-US", "User-Agent": "Shan-yan-profile"})
    with urlopen(request, timeout=15) as response:
        days = recent_contributions(response.read().decode("utf-8"))
    CHART_PATH.write_text(render_chart(days), encoding="utf-8")


if __name__ == "__main__":
    main()
