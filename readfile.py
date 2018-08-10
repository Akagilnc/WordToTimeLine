from docx import Document
import json
import pprint

document = Document('source.docx')

document = [part.text for part in document.paragraphs]

doc = {}
x = 1
key = ''
value = []
for line in document:
    if line.startswith("{}、".format(x)):
        if key:
            doc[key] = value
        value = []
        key = line
        x += 1
    else:
        value.append(line)

with open('temp.txt', 'w', encoding='utf8') as file:
    json.dump(doc, file, ensure_ascii=False)

for item in doc.items():
    print('title is : ', item[0])
    for event in item[1]:
        print("    event is:", event)
