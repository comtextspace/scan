import json
import os

# 3-rd party
from ruamel.yaml import YAML


SOURCE_FILENAME = os.path.join('.', 'archives.yml')
DEST_FILENAME = os.path.join('.', 'template', 'scans.json')

yaml = YAML(typ='safe')
archives = yaml.load(open(SOURCE_FILENAME, encoding='utf-8'))

scans_json = {
    'data': []
}

for item in archives:
    title = item['title']
    link = item['link']
    category = item['category']
    type = item['type']
    lang = item['lang']
    item_amount = item['item_amount']
    platform = item['platform']
    platform_link = item['platform_link']

    scans_json['data'].append([
        f'<a href="{link}">{title}</a>',
        category,
        type,
        lang,
        item_amount,
        f'<a href="{platform_link}">{platform}</a>' if platform_link else platform,
    ])

file = open(DEST_FILENAME, 'w', encoding='utf-8')
file.write(json.dumps(scans_json, indent=4, ensure_ascii=False))
