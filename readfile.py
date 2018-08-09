from docx import Document
import pprint

document = Document('source.docx')

document = [part.text for part in document.paragraphs]

pprint.pprint(document)


