from docx import Document
import json
import pprint

document = Document('source.docx')

document = [part.text for part in document.paragraphs]

def time_arrangement(event):
    z = event.find('）')
    y = event.find('，')
    return event[z+1:y]

def onlynum(date):
    year = date[0:4]
    n = date.find('年')
    m = date.find('月')
    month = date[n+1:m]
    r = date.find('日')
    day = date[m+1:r]
    date = year+month+day
    return date

doc = {}
x = 1
key = ''
value = []
time_list = []
key_2 = ''
doc_2 = {}

for line in document:
    if line.startswith("{}、".format(x)):
        if key :
            doc[key] = value
        value = []
        key = line
        #print(key)
        x += 1
    else:
        value.append(line)
        if key:
            if time_arrangement(line):
                key_2 = time_arrangement(line)
                doc_2[key_2] = line
                #print(doc_2)
                time_list.append(key_2)
                list.sort(time_list)

for number in time_list:
    print(number)
    print(doc_2[number])







                #data.sort(key=lambda x: x["create_time"])

#with open('temp.txt', 'w', encoding='utf8') as file:
   # json.dump(doc, file, ensure_ascii=False)
