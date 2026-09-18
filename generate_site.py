# -*- coding: utf-8 -*-
"""고기타임 정적 사이트 생성기 — 공통 템플릿 + 데이터로 전체 페이지를 만든다."""
import os

SITE_NAME = "고기타임"
SITE_TAGLINE = "부위별 고기 굽는 시간·온도 가이드"
SITE_URL = "https://jinaplus-svg.github.io"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

NAV_LINKS = [
    ("index.html", "홈"),
    ("calculator.html", "굽기 계산기"),
    ("game.html", "타이밍 게임"),
    ("about.html", "소개"),
]

GUIDES = [
    {
        "slug": "beef-doneness-guide",
        "title": "소고기 굽기 단계별 온도 완벽 정리 (레어~웰던)",
        "desc": "레어, 미디엄레어, 미디엄, 미디엄웰, 웰던까지 소고기 굽기 단계별 내부 온도와 특징을 표로 정리했습니다.",
        "keywords": "소고기 굽기 온도, 스테이크 굽기 단계, 레어 미디엄 웰던 온도",
        "intro": "스테이크를 구울 때 가장 많이 헷갈리는 부분이 바로 \"굽기 단계별 온도\"입니다. 식당마다 부르는 이름은 비슷한데 막상 집에서 구우면 원하는 정도로 맞추기가 쉽지 않죠. 아래 표에 각 단계별 목표 내부 온도와 고기 상태를 정리했습니다.",
        "table_headers": ["굽기 단계", "내부 온도", "고기 상태"],
        "table_rows": [
            ["레어 (Rare)", "49~52°C", "중심부가 붉고 차가운 느낌, 겉면만 익음"],
            ["미디엄레어 (Medium Rare)", "52~57°C", "중심부가 선홍색, 육즙이 가장 풍부한 구간"],
            ["미디엄 (Medium)", "57~63°C", "중심부가 분홍색, 대중적으로 가장 선호되는 단계"],
            ["미디엄웰 (Medium Well)", "63~68°C", "중심부에 옅은 분홍기만 남음"],
            ["웰던 (Well Done)", "68°C 이상", "중심부까지 회갈색, 육즙이 가장 적음"],
        ],
        "tips": [
            "고기는 불에서 내린 후에도 내부 온도가 2~3°C 더 올라갑니다(잔열 조리) — 목표보다 살짝 낮을 때 불에서 내리세요.",
            "온도계는 고기의 가장 두꺼운 부분 중앙에 찔러 측정하는 것이 정확합니다.",
            "냉장고에서 바로 꺼낸 고기는 목표 온도에 도달하는 시간이 길어지므로, 굽기 20~30분 전 상온에 꺼내두면 더 균일하게 익습니다.",
        ],
        "related": ["beef-steak-pan", "beef-steak-oven", "meat-rest-time-guide"],
    },
    {
        "slug": "beef-steak-pan",
        "title": "소고기 스테이크 팬에 굽는 시간 (두께별 타이머)",
        "desc": "등심, 안심, 티본 등 두께별로 팬에서 몇 분씩 구워야 하는지 미디엄레어 기준으로 정리했습니다.",
        "keywords": "스테이크 팬 굽기 시간, 등심 굽는 시간, 안심 스테이크 굽기",
        "intro": "팬 스테이크는 두께에 따라 굽는 시간이 크게 달라집니다. 아래는 강불로 예열한 팬 기준, 미디엄레어를 목표로 한 앞뒤 총 굽기 시간의 대략적인 가이드입니다.",
        "table_headers": ["두께", "앞면", "뒷면", "레스팅"],
        "table_rows": [
            ["2cm 미만 (얇은 등심)", "2분", "1분 30초", "3분"],
            ["2~3cm (일반 등심/안심)", "3분", "2분 30초", "5분"],
            ["3~4cm (두꺼운 스테이크)", "4분", "3분 30초", "7분"],
            ["4cm 이상 (티본/포터하우스)", "5분 + 오븐 마무리 권장", "-", "8~10분"],
        ],
        "tips": [
            "팬은 고기를 올리기 전 충분히(연기가 살짝 날 정도로) 예열해야 겉면이 빠르게 시어링됩니다.",
            "4cm 이상 두꺼운 스테이크는 팬으로만 익히면 겉이 타기 쉬우니, 겉면만 시어링한 뒤 오븐(180°C)에서 마무리하는 것을 추천합니다.",
            "정확한 굽기 정도가 중요하다면 시간보다 온도계를 활용하세요 — 위 시간은 두께와 화력에 따라 오차가 있을 수 있습니다.",
        ],
        "related": ["beef-doneness-guide", "beef-steak-oven", "meat-rest-time-guide"],
    },
    {
        "slug": "beef-steak-oven",
        "title": "오븐으로 스테이크 굽는 시간 (리버스 시어 방법)",
        "desc": "오븐에서 저온으로 천천히 익힌 뒤 팬에 시어링하는 '리버스 시어' 방식의 시간과 온도를 정리했습니다.",
        "keywords": "스테이크 오븐 굽기, 리버스 시어, 오븐 스테이크 온도",
        "intro": "두꺼운 스테이크는 오븐에서 저온으로 서서히 익힌 뒤 마지막에 팬이나 토치로 겉면만 강하게 시어링하는 '리버스 시어' 방식이 훨씬 균일하게 익습니다.",
        "table_headers": ["두께", "오븐 온도", "예상 시간(미디엄레어 기준)"],
        "table_rows": [
            ["2~3cm", "120°C", "15~20분"],
            ["3~4cm", "120°C", "20~25분"],
            ["4cm 이상", "110°C", "25~35분"],
        ],
        "tips": [
            "오븐에서 목표 온도보다 5°C 낮게 뺀 뒤, 팬 시어링 단계에서 온도가 조금 더 올라간다는 점을 감안하세요.",
            "오븐에 넣기 전 겉면의 수분을 키친타월로 완전히 제거하면 마지막 시어링이 훨씬 잘 됩니다.",
            "오븐용 온도계를 사용하면 모델별 실제 온도 편차를 줄일 수 있습니다.",
        ],
        "related": ["beef-doneness-guide", "beef-steak-pan", "meat-rest-time-guide"],
    },
    {
        "slug": "pork-belly-grill",
        "title": "삼겹살 직화/에어프라이어 굽는 시간",
        "desc": "삼겹살을 직화 그릴, 팬, 에어프라이어로 구울 때 각각 몇 분이 걸리는지 두께별로 정리했습니다.",
        "keywords": "삼겹살 굽는 시간, 삼겹살 에어프라이어, 삼겹살 직화",
        "intro": "삼겹살은 두께와 조리 기구에 따라 시간 차이가 큽니다. 돼지고기는 소고기와 달리 완전히 익혀야 안전하므로(중심 온도 71°C 이상 권장) 아래 시간은 최소 기준으로 참고하세요.",
        "table_headers": ["조리 방법", "두께", "예상 시간"],
        "table_rows": [
            ["직화 그릴/팬", "1cm 내외(일반 슬라이스)", "앞뒤 각 2~3분"],
            ["직화 그릴/팬", "1.5~2cm(두툼한 슬라이스)", "앞뒤 각 4~5분"],
            ["에어프라이어 200°C", "1cm 내외", "12~15분(중간에 한 번 뒤집기)"],
            ["에어프라이어 200°C", "1.5~2cm", "16~20분(중간에 한 번 뒤집기)"],
        ],
        "tips": [
            "돼지고기는 중심부까지 완전히 익혀야 합니다(핑크빛이 남지 않도록).",
            "에어프라이어는 기종별 화력 차이가 커서, 처음 조리 시 5분 남기고 상태를 확인하는 것을 추천합니다.",
            "구운 후 키친타월에 올려 여분의 기름을 빼면 더 담백하게 즐길 수 있습니다.",
        ],
        "related": ["bacon-oven-airfryer", "pork-tenderloin-oven", "meat-rest-time-guide"],
    },
    {
        "slug": "pork-tenderloin-oven",
        "title": "돼지고기 안심(텐더로인) 오븐 굽는 시간·온도",
        "desc": "퍽퍽해지기 쉬운 돼지고기 안심을 오븐으로 촉촉하게 굽는 시간과 목표 온도를 정리했습니다.",
        "keywords": "돼지안심 오븐 굽기, 텐더로인 조리, 돼지고기 안심 온도",
        "intro": "돼지고기 안심은 지방이 적어 과하게 익히면 금방 퍽퍽해집니다. 목표 내부 온도(63°C, 이후 레스팅으로 71°C 이상 도달)를 지키는 것이 핵심입니다.",
        "table_headers": ["무게", "오븐 온도", "예상 시간"],
        "table_rows": [
            ["300~400g", "200°C", "18~22분"],
            ["400~600g", "200°C", "22~28분"],
            ["600g 이상", "190°C", "28~35분"],
        ],
        "tips": [
            "오븐에 넣기 전 겉면을 팬에서 살짝 시어링하면 풍미와 색이 훨씬 좋아집니다.",
            "63°C에서 꺼내 10분 레스팅하면 잔열로 71°C 안전 기준을 충족하면서도 촉촉함을 유지할 수 있습니다.",
            "무게가 다르면 시간도 비례해 조정하세요 — 위 표는 일반적인 원통형 안심 기준입니다.",
        ],
        "related": ["pork-belly-grill", "meat-rest-time-guide", "chicken-whole-oven"],
    },
    {
        "slug": "chicken-breast-airfryer",
        "title": "닭가슴살 에어프라이어 굽는 시간 (퍽퍽하지 않게)",
        "desc": "닭가슴살을 에어프라이어로 촉촉하게 굽는 시간과 온도, 두께별 차이를 정리했습니다.",
        "keywords": "닭가슴살 에어프라이어, 닭가슴살 굽는 시간, 닭가슴살 촉촉하게",
        "intro": "닭가슴살이 퍽퍽해지는 가장 큰 원인은 '과조리'입니다. 목표 내부 온도(74°C)에 도달하는 즉시 꺼내는 것이 촉촉함의 핵심입니다.",
        "table_headers": ["두께/무게", "온도", "예상 시간"],
        "table_rows": [
            ["150g 내외(일반 두께)", "180°C", "12~14분(중간에 뒤집기)"],
            ["200g 이상(두꺼운 가슴살)", "180°C", "15~18분(중간에 뒤집기)"],
            ["나비 컷(반으로 저민 것)", "180°C", "8~10분"],
        ],
        "tips": [
            "조리 전 소금물에 20~30분 담가두면(브라이닝) 훨씬 촉촉해집니다.",
            "두께가 균일하지 않다면 두꺼운 부분을 밀대로 살짝 눌러 펴주면 고르게 익습니다.",
            "온도계로 74°C를 확인하고 꺼내는 것이 시간보다 훨씬 정확합니다.",
        ],
        "related": ["chicken-whole-oven", "pork-tenderloin-oven"],
    },
    {
        "slug": "chicken-whole-oven",
        "title": "통닭 오븐 굽는 시간 (무게별 로스트 치킨 가이드)",
        "desc": "통닭을 오븐에 로스트할 때 무게별로 몇 분이 걸리는지, 목표 온도는 얼마인지 정리했습니다.",
        "keywords": "통닭 오븐 굽기, 로스트치킨 시간, 통닭 굽는 온도",
        "intro": "통닭은 무게에 비례해서 조리 시간을 계산하는 것이 가장 정확합니다. 일반적으로 500g당 20~25분을 기준으로 잡습니다.",
        "table_headers": ["무게", "오븐 온도", "예상 시간"],
        "table_rows": [
            ["1kg 내외", "190°C", "50~60분"],
            ["1.3~1.5kg", "190°C", "65~80분"],
            ["1.8kg 이상", "180°C", "85~100분"],
        ],
        "tips": [
            "가장 두꺼운 부위인 허벅지 안쪽 온도가 74°C 이상이면 완전히 익은 것입니다.",
            "굽는 중간(전체 시간의 절반 지점)에 팬 육즙을 겉면에 발라주면 훨씬 촉촉하고 색이 좋아집니다.",
            "조리 후 10~15분 레스팅하면 육즙이 고르게 분산됩니다.",
        ],
        "related": ["chicken-breast-airfryer", "meat-rest-time-guide"],
    },
    {
        "slug": "lamb-chop-pan",
        "title": "양고기 립찹 팬 굽는 시간",
        "desc": "양고기 특유의 향을 살리면서 미디엄레어로 굽는 팬 조리 시간을 정리했습니다.",
        "keywords": "양고기 립찹 굽기, 양갈비 굽는 시간, 램찹 조리법",
        "intro": "양고기 립찹은 두께가 얇은 편이라 소고기 스테이크보다 훨씬 빨리 익습니다. 강불에서 짧고 강하게 굽는 것이 핵심입니다.",
        "table_headers": ["두께", "굽기 목표", "앞/뒤 각 시간"],
        "table_rows": [
            ["1.5~2cm", "미디엄레어", "각 2분 30초"],
            ["2~3cm", "미디엄레어", "각 3분 30초"],
            ["2~3cm", "미디엄", "각 4분 30초"],
        ],
        "tips": [
            "양고기는 마늘, 로즈마리와 함께 버터를 끼얹으며 구우면(베이스팅) 풍미가 훨씬 좋아집니다.",
            "지방층이 있는 쪽은 옆으로 세워 1분 정도 먼저 지져 지방을 녹여내면 잡내가 줄어듭니다.",
            "레스팅은 3~5분이면 충분합니다.",
        ],
        "related": ["beef-doneness-guide", "meat-rest-time-guide"],
    },
    {
        "slug": "bacon-oven-airfryer",
        "title": "베이컨 오븐/에어프라이어 굽는 시간",
        "desc": "베이컨을 바삭하게 굽는 오븐과 에어프라이어 시간을 정리했습니다.",
        "keywords": "베이컨 굽는 시간, 베이컨 에어프라이어, 베이컨 오븐 바삭하게",
        "intro": "베이컨은 팬보다 오븐이나 에어프라이어로 구우면 기름이 덜 튀고 두께도 균일하게 익습니다.",
        "table_headers": ["조리 방법", "온도", "예상 시간"],
        "table_rows": [
            ["오븐", "200°C", "15~20분(중간 뒤집기 불필요)"],
            ["에어프라이어", "180°C", "8~10분"],
            ["두꺼운 후제 베이컨(에어프라이어)", "180°C", "10~12분"],
        ],
        "tips": [
            "오븐 사용 시 종이호일을 깔면 기름 정리가 훨씬 편합니다.",
            "베이컨끼리 겹치지 않게 펼쳐야 고르게 바삭해집니다.",
            "원하는 바삭함보다 살짝 덜 익었을 때 꺼내세요 — 식으면서 더 바삭해집니다.",
        ],
        "related": ["pork-belly-grill"],
    },
    {
        "slug": "salmon-pan-oven",
        "title": "연어 굽기 시간 (팬/오븐 비교)",
        "desc": "연어를 팬과 오븐으로 각각 구울 때 두께별 시간과 목표 온도를 정리했습니다.",
        "keywords": "연어 굽는 시간, 연어 팬 굽기, 연어 오븐 온도",
        "intro": "연어는 과하게 익히면 퍽퍽해지고 부서지기 쉬운 생선입니다. 껍질 쪽부터 구워 바삭함을 살리는 것이 포인트입니다.",
        "table_headers": ["조리 방법", "두께", "예상 시간"],
        "table_rows": [
            ["팬(껍질 있는 필렛)", "2cm 내외", "껍질 4분 + 반대면 2분"],
            ["오븐 200°C", "2~3cm", "12~15분"],
            ["오븐 200°C(포일 포장)", "2~3cm", "15~18분"],
        ],
        "tips": [
            "목표 내부 온도는 52~57°C(미디엄) 정도로, 살짝 덜 익은 듯할 때 꺼내는 것이 좋습니다.",
            "껍질을 바삭하게 하려면 조리 전 겉면 수분을 완전히 제거하세요.",
            "포일로 감싸 오븐에 구우면 촉촉함이 극대화되지만 껍질은 바삭해지지 않습니다.",
        ],
        "related": ["meat-rest-time-guide"],
    },
    {
        "slug": "meat-rest-time-guide",
        "title": "고기 구운 후 레스팅 시간 가이드 (왜 꼭 필요할까)",
        "desc": "고기를 굽고 나서 바로 자르지 말고 레스팅해야 하는 이유와 부위별 권장 레스팅 시간을 정리했습니다.",
        "keywords": "고기 레스팅, 스테이크 레스팅 시간, 고기 굽고 쉬는 이유",
        "intro": "레스팅(resting)은 구운 고기를 바로 자르지 않고 몇 분간 그대로 두는 과정입니다. 이 과정을 건너뛰면 자르는 순간 육즙이 전부 빠져나가 퍽퍽해집니다.",
        "table_headers": ["고기 종류/크기", "권장 레스팅 시간"],
        "table_rows": [
            ["얇은 스테이크(2cm 미만)", "3분"],
            ["일반 스테이크(2~4cm)", "5~7분"],
            ["두꺼운 로스트/통닭", "10~15분"],
            ["닭가슴살/작은 부위", "3~5분"],
        ],
        "tips": [
            "레스팅 중 고기를 알루미늄 포일로 느슨하게 덮어두면 온도를 유지하면서도 겉면이 눅눅해지지 않습니다.",
            "레스팅하는 동안 잔열로 내부 온도가 2~5°C 더 올라간다는 점을 굽기 목표 온도 계산에 반영하세요.",
            "너무 오래 레스팅하면(15분 이상) 고기가 식어버리니 적정 시간을 지키는 것이 중요합니다.",
        ],
        "related": ["beef-doneness-guide", "beef-steak-pan", "beef-steak-oven"],
    },
]

GUIDE_BY_SLUG = {g["slug"]: g for g in GUIDES}


def nav_html(active_href=""):
    items = []
    for href, label in NAV_LINKS:
        cls = ' class="active"' if href == active_href else ""
        items.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(items)


def page_shell(title, description, keywords, body_html, active_href="", extra_head="", path=""):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="google-adsense-account" content="ca-pub-9998958180062429">
<meta name="naver-site-verification" content="4d4276eb90133b03378f5240e9ea892d529d4240" />
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{SITE_URL}/{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="style.css">
{extra_head}</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">🍖 {SITE_NAME}</a>
    <nav>
      {nav_html(active_href)}
    </nav>
  </div>
</header>
<main class="wrap">
{body_html}
</main>
<div class="ad-slot" aria-label="advertisement">
  <!-- 광고 영역: 애드센스 승인 후 이 위치에 광고 코드를 삽입하세요 -->
  <span class="ad-slot-label">광고</span>
</div>
<footer class="site-footer">
  <div class="wrap">
    <p>&copy; 2026 {SITE_NAME}. 이 사이트의 조리 시간은 일반적인 기준을 안내하는 참고용 정보이며,
    고기 두께·화력·기기 성능에 따라 실제 시간은 달라질 수 있습니다.</p>
    <p><a href="about.html">소개</a> · <a href="privacy.html">개인정보처리방침</a></p>
  </div>
</footer>
</body>
</html>
"""


def render_table(headers, rows):
    thead = "".join(f"<th>{h}</th>" for h in headers)
    trs = []
    for row in rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        trs.append(f"<tr>{tds}</tr>")
    return f"""<div class="table-wrap">
<table>
<thead><tr>{thead}</tr></thead>
<tbody>
{''.join(trs)}
</tbody>
</table>
</div>"""


def render_guide_page(g):
    related_links = "\n".join(
        f'<li><a href="{slug}.html">{GUIDE_BY_SLUG[slug]["title"]}</a></li>'
        for slug in g["related"] if slug in GUIDE_BY_SLUG
    )
    tips_html = "\n".join(f"<li>{t}</li>" for t in g["tips"])
    body = f"""
<article class="guide">
  <h1>{g['title']}</h1>
  <p class="intro">{g['intro']}</p>
  {render_table(g['table_headers'], g['table_rows'])}
  <h2>실전 팁</h2>
  <ul class="tips">
{tips_html}
  </ul>
  <p class="disclaimer">※ 위 시간과 온도는 일반적인 조리 환경을 기준으로 한 참고용 안내입니다. 고기의 두께, 초기 온도(냉장/상온), 조리 기구의 화력에 따라 실제로는 차이가 날 수 있으니 온도계 사용을 권장합니다.</p>
  <h2>관련 가이드</h2>
  <ul class="related-list">
{related_links}
  </ul>
  <p><a class="cta" href="calculator.html">→ 내 고기 무게로 직접 계산해보기</a></p>
</article>
"""
    return page_shell(g["title"], g["desc"], g["keywords"], body, path=f"{g['slug']}.html")


def render_index():
    cards = []
    for g in GUIDES:
        cards.append(f'<a class="card" href="{g["slug"]}.html"><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>')
    body = f"""
<section class="hero">
  <h1>고기 굽는 시간, 이제 매번 검색하지 마세요</h1>
  <p>부위별·조리 방법별 굽기 시간과 온도를 한곳에 정리했습니다. 소고기, 돼지고기, 닭고기, 양고기, 생선까지
  실전에서 바로 쓸 수 있는 표와 팁만 담았습니다.</p>
  <div class="hero-actions">
    <a class="cta" href="calculator.html">🔥 굽기 시간 계산기 써보기</a>
    <a class="cta secondary" href="game.html">🎮 고기 타이밍 챌린지 게임</a>
  </div>
</section>
<section>
  <h2>가이드 목록</h2>
  <div class="card-grid">
    {''.join(cards)}
  </div>
</section>
"""
    return page_shell(f"{SITE_NAME} - {SITE_TAGLINE}", SITE_TAGLINE + ". 소고기·돼지고기·닭고기·양고기·생선 굽는 시간과 온도를 한눈에.",
                       "고기 굽는 시간, 스테이크 굽기, 삼겹살 굽기, 닭가슴살 굽기", body, active_href="index.html", path="")


def render_about():
    body = """
<article class="guide">
  <h1>고기타임 소개</h1>
  <p>고기타임은 "매번 검색하기 귀찮았던" 고기 굽는 시간과 온도를 한곳에 정리한 참고 사이트입니다.
  스테이크, 삼겹살, 닭가슴살, 통닭, 양갈비, 연어까지 자주 검색되는 조리법을 표와 실전 팁으로 정리했습니다.</p>
  <p>모든 정보는 일반적으로 통용되는 조리 가이드라인을 바탕으로 작성되었으며, 실제 결과는 고기 상태와
  조리 기구에 따라 달라질 수 있습니다. 정확한 굽기를 원하신다면 조리용 온도계 사용을 권장합니다.</p>
  <p>문의: contact@example.com</p>
</article>
"""
    return page_shell("사이트 소개", f"{SITE_NAME} 소개 페이지입니다.", "고기타임 소개", body, active_href="about.html", path="about.html")


def render_privacy():
    body = """
<article class="guide">
  <h1>개인정보처리방침</h1>
  <p>본 사이트는 Google AdSense를 비롯한 제3자 광고 서비스를 이용할 수 있으며, 이러한 서비스는 사용자의
  방문 기록을 기반으로 맞춤 광고를 게재하기 위해 쿠키를 사용할 수 있습니다.</p>
  <p>Google을 포함한 제3자 공급업체는 쿠키를 사용하여 사용자의 이전 방문 기록을 기반으로 광고를 게재합니다.
  사용자는 Google 광고 설정 페이지를 방문하여 맞춤 광고를 거부할 수 있습니다.</p>
  <p>본 사이트는 이름, 이메일 등 개인을 식별할 수 있는 정보를 별도로 수집하지 않습니다.</p>
  <p>본 방침은 사전 고지 없이 변경될 수 있습니다. 최종 수정일: 2026년 9월.</p>
</article>
"""
    return page_shell("개인정보처리방침", f"{SITE_NAME} 개인정보처리방침입니다.", "개인정보처리방침", body, active_href="", path="privacy.html")


def render_calculator():
    body = """
<article class="guide">
  <h1>고기 굽기 시간 계산기</h1>
  <p class="intro">고기 종류와 두께(또는 무게), 조리 방법을 선택하면 대략적인 굽기 시간을 계산해 드립니다.
  실제 시간은 화력과 초기 온도에 따라 달라질 수 있으니 참고용으로 사용하세요.</p>

  <div class="calc-box">
    <label>고기 종류
      <select id="meatType">
        <option value="beef_steak">소고기 스테이크 (두께 기준, cm)</option>
        <option value="pork_belly">삼겹살 (두께 기준, cm)</option>
        <option value="chicken_breast">닭가슴살 (무게 기준, g)</option>
        <option value="whole_chicken">통닭 (무게 기준, kg)</option>
      </select>
    </label>
    <label id="sizeLabel">두께 (cm)
      <input type="number" id="sizeInput" value="2.5" step="0.1" min="0.5">
    </label>
    <label>조리 방법
      <select id="method">
        <option value="pan">팬/직화</option>
        <option value="oven">오븐</option>
        <option value="airfryer">에어프라이어</option>
      </select>
    </label>
    <button id="calcBtn" class="cta">계산하기</button>
  </div>

  <div id="result" class="calc-result" hidden>
    <h2>예상 조리 시간</h2>
    <p id="resultText"></p>
  </div>

  <p class="disclaimer">※ 이 계산기는 일반적인 경험칙에 기반한 추정치입니다. 실제 조리 시 온도계로 최종 확인하세요.</p>
</article>

<script>
const sizeLabel = document.getElementById('sizeLabel');
const meatType = document.getElementById('meatType');
const sizeInput = document.getElementById('sizeInput');

const labelMap = {
  beef_steak: '두께 (cm)',
  pork_belly: '두께 (cm)',
  chicken_breast: '무게 (g)',
  whole_chicken: '무게 (kg)',
};
const defaultMap = { beef_steak: 2.5, pork_belly: 1.5, chicken_breast: 150, whole_chicken: 1.3 };

meatType.addEventListener('change', () => {
  sizeLabel.childNodes[0].textContent = labelMap[meatType.value] + ' ';
  sizeInput.value = defaultMap[meatType.value];
});

function estimate(type, size, method) {
  // 매우 단순화된 경험칙 기반 추정 — 실전 가이드 페이지의 표를 근사한 값
  if (type === 'beef_steak') {
    const perCm = method === 'oven' ? 8 : 2.2;
    const base = method === 'oven' ? 5 : 0;
    const minutes = Math.round(base + size * perCm);
    return `${method === 'oven' ? '오븐 120°C' : '팬 강불'} 기준 총 약 ${minutes}분 (앞뒤 합산, 미디엄레어 목표) + 레스팅 5분`;
  }
  if (type === 'pork_belly') {
    const perCm = method === 'airfryer' ? 9 : 2.8;
    const minutes = Math.round(size * perCm);
    return `${method === 'airfryer' ? '에어프라이어 200°C' : '직화/팬'} 기준 총 약 ${minutes}분 (완전히 익을 때까지)`;
  }
  if (type === 'chicken_breast') {
    const perG = 0.08;
    const minutes = Math.round(size * perG + (method === 'oven' ? 4 : 0));
    return `${method === 'oven' ? '오븐 190°C' : '에어프라이어 180°C'} 기준 총 약 ${minutes}분 (중심 온도 74°C 확인)`;
  }
  if (type === 'whole_chicken') {
    const perKg = 45;
    const minutes = Math.round(size * perKg + 15);
    return `오븐 190°C 기준 총 약 ${minutes}분 (허벅지 안쪽 74°C 이상 확인)`;
  }
  return '계산할 수 없습니다.';
}

document.getElementById('calcBtn').addEventListener('click', () => {
  const type = meatType.value;
  const size = parseFloat(sizeInput.value) || 0;
  const method = document.getElementById('method').value;
  const text = estimate(type, size, method);
  document.getElementById('resultText').textContent = text;
  document.getElementById('result').hidden = false;
});
</script>
"""
    return page_shell("고기 굽기 시간 계산기", "고기 종류와 두께·무게를 입력하면 예상 굽기 시간을 계산해줍니다.",
                       "고기 굽기 계산기, 스테이크 시간 계산", body, active_href="calculator.html", path="calculator.html")


def write(path, content):
    with open(os.path.join(OUT_DIR, path), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


def main():
    for g in GUIDES:
        write(f"{g['slug']}.html", render_guide_page(g))
    write("index.html", render_index())
    write("about.html", render_about())
    write("privacy.html", render_privacy())
    write("calculator.html", render_calculator())
    print(f"\n총 {len(GUIDES)}개 가이드 페이지 + index/about/privacy/calculator 생성 완료")


if __name__ == "__main__":
    main()
