import json
import os

# 3-rd party
from ruamel.yaml import YAML
import requests


SOURCE_FILENAME = os.path.join('.', 'archives.yml')

yaml = YAML(typ='safe')
archives = yaml.load(open(SOURCE_FILENAME, encoding='utf-8'))

invalid_link = []
visited = set()


def check_link(link):
    if link is None:
        return

    link = link.strip()

    if len(link) == 0:
        return

    if link in visited:
        return

    print('check ' + link)
    visited.add(link)

    try:
        r = requests.get(link)
    except Exception as e:
        invalid_link.append((link, e.message))
        return

    if r.status_code != 200:
        invalid_link.append((link, r.status_code))


for archive in archives:
    link = archive['link']
    check_link(link)

    link = archive['platform_link']
    check_link(link)


print(invalid_link)
