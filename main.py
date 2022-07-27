from random import randint
from PyPDF2 import PdfFileWriter, PdfFileReader
from boardadder import *
from pdfAdder import *
from six import BytesIO
import io
import os

numboards = 25


def setT():
    return [["images/"+os.listdir("images")[i], i + 1]
            for i in range(len(os.listdir("images")))]


things = setT()

board = [["" for c in range(5)] for r in range(5)]

page = pdf("test")


def remove(h, c, r):
    x = randint(0, len(h) - 1)
    m = h[x]
    del things[x]
    
    page.addImg(m[0], c, r, m[1])
    
    return str(m)


def p(g):
    return str(" " + str(g)[1:][:-1].replace("],", "],\n"))


#page.create_pdf("Hello:")
#page.add_image()

for i in range(numboards):
    things = setT()
    board = [[
        remove(things, c, r) if
        (c != 2 or r != 2) else remove([['free.jpeg', " "]], c, r) for c in range(5)
    ] for r in range(5)]
    page.show()

page.save()






source = PdfFileReader('test.pdf')
writer = PdfFileWriter()

# Merge sorce and watermark pages
page0 = source.getPage(0)
page0.mergePage(source.getPage(1))
writer.insertPage(page0, 0)

# Write result to file
with open('merged.pdf', 'wb') as fp:
    writer.write(fp)

print("done")
