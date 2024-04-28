#!/usr/bin/python3
import sys
import os
import xml.etree.ElementTree as ET

def parse(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    remotes = {}
    projects = []
    for child in root:
        if child.tag == 'remote':
            fetch = child.attrib['fetch']
            name  = child.attrib['name']
            remotes[name] = fetch
        elif child.tag == 'project':
            projects.append(child.attrib)

    # print(remotes)
    # print(projects)
    for project in projects:
        remote = project['remote']
        name   = project['name']
        url_base = remotes[remote]
        url = os.path.join(url_base, name)
        print(url)

if __name__ == '__main__':
    parse(sys.argv[1])
