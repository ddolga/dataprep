import os
from openpyxl import Workbook


class Accumulator(object):
    toWb = None
    toWs = None
    totals = []
    map = []
    startCol = 0

    headers = ["Year", "School Id", "Category", "Number"]

    def __init__(self,  startCol):
        self.toWb = Workbook(write_only=True)
        self.startCol = startCol
        self.reset()


    def reset(self):
        self.totals = []
        self.initTotalsArray()

    def initTotalsArray(self):
        for m in self.map:
            self.totals.append(0)


    def newSheet(self, title):
        self.toWs = self.toWb.create_sheet()
        self.toWs.title = title
        self.writeHeaders()


    def accumulateRow(self, row):

        for i in range(0, len(self.map)):
            self.totals[i] += row[self.startCol + i].value


    def appendRow(self, year, schoolId):
        for i in range(0, len(self.map)):
            newRow = []
            newRow.append(year)  # year
            newRow.append(schoolId)  # school id
            newRow.append(self.map[i])
            newRow.append(self.totals[i])
            self.toWs.append(newRow)

        self.reset();


    def writeHeaders(self):
        head_row = []
        for h in self.headers:
            head_row.append(h)

        self.toWs.append(head_row)


    def writeFile(self, filename, type):
        fp = os.path.splitext(filename)
        fn = fp[0] + "_" + type + "_converted" + fp[1]
        print("Saving file: " + fn)
        self.toWb.save(fn)
