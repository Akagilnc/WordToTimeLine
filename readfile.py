from docx import Document
import pprint

document = Document('source.docx')


pprint.pprint([part.text for part in document.paragraphs])
