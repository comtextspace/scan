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
    scans_json['data'].append(list(item.values()))

file = open(DEST_FILENAME, 'w', encoding='utf-8')
file.write(json.dumps(scans_json, indent=4, ensure_ascii=False))
