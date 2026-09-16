# -*- coding: utf-8 -*-
import os

SITE_URL = "https://jinaplus-svg.github.io"
PAGES = [
    "", "beef-doneness-guide.html", "beef-steak-pan.html", "beef-steak-oven.html",
    "pork-belly-grill.html", "pork-tenderloin-oven.html", "chicken-breast-airfryer.html",
    "chicken-whole-oven.html", "lamb-chop-pan.html", "bacon-oven-airfryer.html",
    "salmon-pan-oven.html", "meat-rest-time-guide.html", "calculator.html", "game.html",
    "about.html", "privacy.html",
]

urls = "\n".join(f"  <url><loc>{SITE_URL}/{p}</loc></url>" for p in PAGES)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)
print("wrote sitemap.xml with", len(PAGES), "urls")

robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)
print("wrote robots.txt")
