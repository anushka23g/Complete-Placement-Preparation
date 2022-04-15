import PyPDF2
file_name = "<PDF NAME>.pdf"
PDFFile = open(file_name,'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

qu = []

nil = []

for page in range(pages):
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                qu.append(u[ank][uri])

set = open('md/'+file_name.split(".pdf")[0]+'.md','r')
lines = set.readlines()
for line in lines:
    nil.append(line)
set = open('md/'+file_name.split(".pdf")[0]+'.md','w')

for i in range(len(nil)):
    set.write('['+nil[i]+']('+qu[i]+')\n\n')