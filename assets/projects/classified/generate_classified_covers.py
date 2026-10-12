#!/usr/bin/env python3
"""Wrap the existing, unchanged cover PNGs in standalone classified SVG cards.

Run with Python 3. No third-party packages or raster image transformations are
used. Each SVG embeds its source PNG byte-for-byte as a base64 data URI.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import struct
from pathlib import Path
from xml.etree import ElementTree as ET


OUTPUT = Path(__file__).resolve().parent
ILLUSTRATED = OUTPUT.parent / "illustrated"
WIDTH, HEIGHT = 1942, 950
IMAGE_X, IMAGE_Y, IMAGE_WIDTH = 36, 148, 1870
FONT = "'PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif"

COVERS = (
    ("fanxiaoyi", "翻小译", "产品", "#6850A1", "#EFE8FA",
     ILLUSTRATED / "fanxiaoyi.png"),
    ("product-foundry", "产品工坊", "产品", "#62518B", "#ECE8F6",
     ILLUSTRATED / "product-foundry.png"),
    ("muse10-ai-nails", "智能美甲共创", "产品", "#A2476A", "#F9E7ED",
     ILLUSTRATED / "muse10-ai-nails.png"),
    ("child-knowledge-cocreation", "儿童故事共创", "产品", "#8F6B2D", "#FBF0D8",
     ILLUSTRATED / "child-knowledge-cocreation.png"),
    ("evidence-led-teardown", "循证产品拆解", "技能", "#487561", "#E7F1E8",
     ILLUSTRATED / "evidence-led-teardown.png"),
    ("muse10-nail-visuals", "十指美甲视觉", "技能", "#9B436B", "#F7E7EF",
     ILLUSTRATED / "muse10-nail-visuals.png"),
    ("open-source-reviews", "开源项目审阅", "文档", "#426AA9", "#E8EFFA",
     ILLUSTRATED / "open-source-reviews.png"),
)


def png_size(blob: bytes) -> tuple[int, int]:
    if blob[:8] != b"\x89PNG\r\n\x1a\n" or blob[12:16] != b"IHDR":
        raise ValueError("Expected a PNG with a valid IHDR")
    return struct.unpack(">II", blob[16:24])


def product_header(accent: str, pale: str) -> str:
    return f'''<g id="category-product" aria-label="产品：应用窗口式顶栏">
    <rect x="36" y="34" width="1870" height="104" rx="24" fill="{pale}"/>
    <g fill="{accent}" opacity="0.7">
      <circle cx="72" cy="86" r="12"/><circle cx="108" cy="86" r="12"/>
      <circle cx="144" cy="86" r="12"/>
    </g>
    <g transform="translate(192 59)" fill="none" stroke="{accent}" stroke-width="5">
      <rect width="54" height="54" rx="13"/>
      <rect x="11" y="11" width="12" height="12" rx="3" fill="{accent}" stroke="none"/>
      <rect x="31" y="11" width="12" height="12" rx="3" fill="{accent}" stroke="none"/>
      <rect x="11" y="31" width="12" height="12" rx="3" fill="{accent}" stroke="none"/>
      <rect x="31" y="31" width="12" height="12" rx="3" fill="{accent}" stroke="none"/>
    </g>
    <text x="274" y="108" font-size="62" font-weight="800" fill="{accent}">产品</text>
    <g stroke="{accent}" stroke-width="5" stroke-linecap="round" fill="none" opacity="0.65">
      <path d="M1750 100h30"/><rect x="1810" y="71" width="30" height="30" rx="5"/>
      <path d="m1865 72 25 25m0-25-25 25"/>
    </g>
  </g>'''


def skill_header(accent: str, pale: str) -> str:
    return f'''<g id="category-skill" aria-label="技能：模块与连接节点">
    <rect x="36" y="34" width="1870" height="104" rx="24" fill="{pale}"/>
    <g transform="translate(65 59)" fill="none" stroke="{accent}" stroke-width="5" stroke-linejoin="round">
      <path d="M27 0 53 15v29L27 59 1 44V15Z"/>
      <path d="m1 15 26 15 26-15M27 30v29"/>
    </g>
    <text x="151" y="108" font-size="62" font-weight="800" fill="{accent}">技能</text>
    <g stroke="{accent}" stroke-width="5" fill="none" stroke-linejoin="round">
      <path d="M1568 86h61m71 0h63"/>
      <rect x="1498" y="54" width="70" height="64" rx="15" fill="#FFFCF7"/>
      <rect x="1629" y="54" width="71" height="64" rx="15" fill="#FFFCF7"/>
      <rect x="1763" y="54" width="70" height="64" rx="15" fill="#FFFCF7"/>
      <circle cx="1533" cy="86" r="9" fill="{accent}" stroke="none"/>
      <path d="m1653 86 9 9 18-20" stroke-linecap="round"/>
      <path d="M1784 77h28m-28 18h19" stroke-linecap="round"/>
      <path d="m1616 78 13 8-13 8m134-16 13 8-13 8"/>
    </g>
  </g>'''


def document_header(accent: str, pale: str) -> str:
    return f'''<g id="category-document" aria-label="文档：纸页与折角">
    <path d="M60 34h1766l80 80v24H60q-24 0-24-24V58q0-24 24-24Z" fill="{pale}"/>
    <path d="M1826 34v56q0 24 24 24h56Z" fill="{accent}" opacity="0.22"/>
    <path d="M1826 35v55q0 24 24 24h54" fill="none" stroke="{accent}" stroke-width="4" opacity="0.5"/>
    <g transform="translate(65 55)" fill="none" stroke="{accent}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
      <path d="M2 8h39l16 16v42H2Z" opacity="0.4"/>
      <path d="M10 0h29l18 18v42H10Z" fill="#FFFCF7"/>
      <path d="M39 0v18h18M21 31h25m-25 13h20"/>
    </g>
    <text x="151" y="108" font-size="62" font-weight="800" fill="{accent}">文档</text>
    <g fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round" opacity="0.65">
      <path d="M1620 66h134m-134 20h104m-104 20h121"/>
    </g>
  </g>'''


HEADERS = {"产品": product_header, "技能": skill_header, "文档": document_header}


def build_card(title: str, category: str, accent: str, pale: str,
               blob: bytes, source_width: int, source_height: int) -> tuple[str, float]:
    image_height = IMAGE_WIDTH * source_height / source_width
    if IMAGE_Y + image_height > HEIGHT - 20:
        raise ValueError("Source does not fit the shared card image area")
    encoded = base64.b64encode(blob).decode("ascii")
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="card-title card-description">
  <title id="card-title">{title} · {category}</title>
  <desc id="card-description">顶部以独立分类栏标识{category}。下方保留原封面的角色、动作和三行中文文案，原图按比例完整展示。</desc>
  <defs>
    <clipPath id="illustration-clip"><rect x="{IMAGE_X}" y="{IMAGE_Y}" width="{IMAGE_WIDTH}" height="{image_height:.6f}" rx="24"/></clipPath>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#FFFCF7"/>
  <rect x="16" y="16" width="1910" height="918" rx="42" fill="#FFFCF7" stroke="{accent}" stroke-width="7"/>
  <g font-family="{FONT}">
  {HEADERS[category](accent, pale)}
  </g>
  <image id="original-illustration" x="{IMAGE_X}" y="{IMAGE_Y}" width="{IMAGE_WIDTH}" height="{image_height:.6f}" preserveAspectRatio="xMidYMid meet" clip-path="url(#illustration-clip)" href="data:image/png;base64,{encoded}"/>
</svg>
'''
    return svg, image_height


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "format": "standalone SVG with unchanged embedded PNG",
        "size": {"width": WIDTH, "height": HEIGHT},
        "classification": {"产品": 4, "技能": 2, "文档": 1},
        "cards": [],
    }
    ns = {"svg": "http://www.w3.org/2000/svg"}
    for identifier, title, category, accent, pale, source in COVERS:
        original = source.read_bytes()
        source_width, source_height = png_size(original)
        original_sha = hashlib.sha256(original).hexdigest()
        svg, image_height = build_card(
            title, category, accent, pale, original, source_width, source_height
        )
        target = OUTPUT / f"{identifier}.svg"
        target.write_text(svg, encoding="utf-8")

        # Validate XML, standalone image bytes, layout separation, and source
        # immutability. These are artifact integrity checks, not pixel editing.
        parsed = ET.parse(target).getroot()
        image_node = parsed.find("svg:image", ns)
        assert image_node is not None
        uri = image_node.attrib["href"]
        assert uri.startswith("data:image/png;base64,")
        embedded = base64.b64decode(uri.split(",", 1)[1], validate=True)
        assert embedded == original
        assert hashlib.sha256(source.read_bytes()).hexdigest() == original_sha
        assert float(image_node.attrib["y"]) > 138
        assert float(image_node.attrib["y"]) + image_height < HEIGHT - 20
        assert parsed.attrib["viewBox"] == f"0 0 {WIDTH} {HEIGHT}"

        manifest["cards"].append({
            "id": identifier,
            "title": title,
            "category": category,
            "file": target.name,
            "source": os.path.relpath(source, OUTPUT),
            "source_size": {"width": source_width, "height": source_height},
            "source_sha256": original_sha,
            "image_box": {"x": IMAGE_X, "y": IMAGE_Y,
                          "width": IMAGE_WIDTH, "height": image_height},
            "svg_bytes": target.stat().st_size,
            "validated": {"xml": True, "original_png_unchanged": True,
                          "embedded_png_exact": True, "header_separate": True},
        })
        print(f"{target.name}: {WIDTH} × {HEIGHT}; {category}; XML and embedded PNG verified")

    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
