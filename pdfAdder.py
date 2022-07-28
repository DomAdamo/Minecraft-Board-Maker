from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.lib.units import inch

FILL = (137, 187, 106)


def inch(i):
    return 72 * i


class pdf:
    def __init__(self, name):
        self.w = 600
        self.name = name + '.pdf'
        self.can = canvas.Canvas(self.name)
        self.can.setFontSize(12)
        self.size = ((self.w / (8.5) * 11 / 2), self.w)
        self.bScale = .85
        self.x_start = abs(self.size[0] - (inch(self.bScale) * 5)) / 2
        self.y_start = 70

        self.start()

    def addImg(self, name, c, r, x):
        imgH = inch(self.bScale * 1.25)
        imgW = inch(self.bScale)

        self.can.setFillColorRGB(1, 1, 1)
        self.can.rect(self.x_start + c * imgW,
                      self.y_start + r * imgH,
                      imgW,
                      imgH,
                      fill=1)

        self.can.drawImage(name,
                           self.x_start + c * imgW,
                           self.y_start + r * imgH,
                           width=imgW,
                           height=imgH,
                           preserveAspectRatio=True,
                           mask='auto')
        self.can.setStrokeColorRGB(.27, .17, .02)

        self.can.drawBoundary(1, self.x_start + c * imgW,
                              self.y_start + r * imgH, imgW, imgH)
        self.can.setStrokeColorRGB(.53, .31, .10)
        self.can.drawBoundary(1, self.x_start + 1 + c * imgW,
                              self.y_start + 1 + r * imgH, imgW - 2, imgH - 2)

        self.can.setFillColorRGB(0, 0, 0)
        self.can.drawString(self.x_start + (c + 1) * imgW - 15,
                            self.y_start + (r + 1) * imgH - 15, str(x))

        self.can._pagesize = self.size

    def start(self):
        self.can.setFillColorRGB(115 / 255, 178 / 255,
                                 84 / 255)  #choose fill colour
        self.can.setStrokeColorRGB(115 / 255, 178 / 255, 84 / 255)
        self.can.rect(0, 0, self.size[0], self.size[1],
                      fill=1)  #draw rectangle
        ts = self.can.drawImage("Title.png",
                                -1000,
                                -1000,
                                self.size[0],
                                preserveAspectRatio=True,
                                mask='auto')
        self.can.drawImage("Title.png",
                           0,
                           self.size[1] - ts[1],
                           self.size[0],
                           preserveAspectRatio=True,
                           mask='auto')
        self.can.drawImage("footer.png",
                           0,
                           0,
                           self.size[0],
                           preserveAspectRatio=True,
                           mask='auto')
        scale = 10
        self.can.setFillColorRGB(1, 1, 1)
        self.can.setStrokeColorRGB(1, 1, 1)
        self.can.rect(self.x_start - scale,
                      self.y_start - scale,
                      inch(1 * self.bScale) * 5 + 2 * scale,
                      inch(1.25 * self.bScale) * 5 + 2 * scale,
                      fill=1)  #draw rectangle

    def show(self):
        self.can.setPageRotation(90)
        self.can._pagesize = (self.size[1], self.size[0])
        self.can.showPage()
        self.start()

    def save(self):

        self.can.save()
