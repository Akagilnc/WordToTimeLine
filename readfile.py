from docx import Document
import json
import pprint

document = Document('source.docx')

document = [part.text for part in document.paragraphs]

def time_arrangement(event):
    z = event.find('）')
    y = event.find('，')
    return event[z+1:y]

doc = {}
x = 1
key = ''
value = []
for line in document:
    if line.startswith("{}、".format(x)):
        if key :
            doc[key] = value
        value = []
        key = line
        x += 1
    else:
        value.append(line)
        key_2 = ''
        doc_2 = {}
        if key:
            if time_arrangement(line):
                key_2 = time_arrangement(line)
                doc_2[key_2] = line

                print(doc_2)



#with open('temp.txt', 'w', encoding='utf8') as file:
   # json.dump(doc, file, ensure_ascii=False)
