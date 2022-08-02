#pre-req: install at CLI --> "pip install xmltodict"
#parses xml file into a Python dict
#xml looks like html format

import xml.etree.ElementTree as ET
import xmltodict #doesnt work sa c9 ide, ubuntu ok.

with open ('doe-a-deer.xml') as fd:
    doc = xmltodict.parse(fd.read())
    print(doc)