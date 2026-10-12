#!/usr/bin/env python3
"""Render the same verified AI news data into the profile and portfolio."""
import argparse
import datetime
import html
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- ai-news:start -->'
END = '<!-- ai-news:end -->'
JS_START = '/* ai-news-data:start */'
JS_END = '/* ai-news-data:end */'

def validate(data):
    datetime.date.fromisoformat(data['updatedAt'])
    assert 1 <= len(data['items']) <= 5, 'Use one to five verified items'
    urls = set()
    for item in data['items']:
        for key in ('title', 'summary', 'eventDate', 'sourceLabel', 'url'):
            assert isinstance(item[key], str) and item[key].strip(), key
        assert datetime.date.fromisoformat(item['eventDate']) <= datetime.date.fromisoformat(data['updatedAt'])
        assert urlparse(item['url']).scheme == 'https' and urlparse(item['url']).netloc
        assert item['url'] not in urls, 'Duplicate news source'
        urls.add(item['url'])

def md(data, heading):
    lines = [heading, '', f"整理日期：**{data['updatedAt']}** · 关注 AI 产品、模型与工具动态。", '']
    for item in data['items']:
        title = item['title'].replace('[', '').replace(']', '')
        lines.extend([f"- **{title}**（事件日期：{item['eventDate']}）", f"  {item['summary']} [查看{item['sourceLabel']}原文]({item['url']})", ''])
    return '\n'.join(lines).rstrip()

def replace_region(text, start, end, content):
    assert text.count(start) == text.count(end) == 1, 'Expected one managed news region'
    return re.sub(re.escape(start) + r'[\s\S]*?' + re.escape(end), lambda _: start + '\n' + content + '\n' + end, text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=Path, required=True)
    args = parser.parse_args()
    source = ROOT / 'data/ai-news.json'
    data = json.loads(source.read_text())
    validate(data)
    archive = ROOT / 'data/news'
    archive.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    (archive / f"{data['updatedAt']}.json").write_text(serialized)
    readme = ROOT / 'README.md'
    content = md(data, '## 📰 每日 AI 资讯') + '\n\n[查看资讯归档 →](AI_NEWS.md) · [个人网站资讯栏目 →](https://wangyangjuan.surge.sh/#news)'
    readme.write_text(replace_region(readme.read_text(), START, END, content))
    days = []
    for path in sorted(archive.glob('*.json'), reverse=True):
        record = json.loads(path.read_text())
        validate(record)
        days.append(md(record, f"## {record['updatedAt']}"))
    (ROOT / 'AI_NEWS.md').write_text('# 每日 AI 资讯归档\n\n以官方原文为主要来源，分别记录整理日期与事件日期。\n\n' + '\n\n'.join(days) + '\n')
    site_index = args.site / 'index.html'
    inline = 'const NEWS = ' + json.dumps(data, ensure_ascii=False, indent=2).replace('<', '\\u003c') + ';'
    site_index.write_text(replace_region(site_index.read_text(), JS_START, JS_END, inline))
    (args.site / 'assets/ai-news.json').write_text(serialized)
    print(f"Synchronized {len(data['items'])} items for {data['updatedAt']}")

if __name__ == '__main__':
    main()
