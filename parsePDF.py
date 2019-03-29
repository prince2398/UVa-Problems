import PyPDF2
import re

def parsePDF(pdf):
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pages = pdfReader.numPages

    for i in range(0,pages):
        pageObj = pdfReader.getPage(i)
        temp = pageObj.extractText()
        print(temp)
        res = re.findall("SampleInput([\S]*)SampleOutput([\S]*)",temp)
        print(res)

with open("a.pdf","rb") as f:
    parsePDF(f)