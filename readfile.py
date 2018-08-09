from docx import Document
import json
import pprint

document = Document('source.docx')

document = [part.text for part in document.paragraphs]

doc = {}
x = 1
key = ''
value = ''
for line in document:
    if line.startswith("{}、".format(x)):
        if key:
            doc[key] = value
        value = ''
        key = line
        x += 1
    else:
        value += line

with open('temp.doc', 'w') as file:
    json.dump(doc, file)
