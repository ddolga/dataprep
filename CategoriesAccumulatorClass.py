from AccumulatorClass import Accumulator


class CategoriesAccumulator(Accumulator):

    teacherTotal = 0
    map = ["I", "II", "III", "IV", "V"]

    def accumulateRow(self, row):

        for i in range(0, len(self.map)):
           self.totals[i] += row[self.startCol + i].value
        self.teacherTotal += row[2].value


    def appendRow(self, year, schoolId):
        allCategories = 0
        for i in range(0, len(self.map)):
            newRow = []
            newRow.append(year)  # year
            newRow.append(schoolId)  # school id
            newRow.append(self.map[i])
            newRow.append(self.totals[i])
            allCategories += self.totals[i]
            self.toWs.append(newRow)

        newRow = []
        newRow.append(year)  # year
        newRow.append(schoolId)  # school id
        newRow.append("0")
        noDegree = self.teacherTotal - allCategories
        newRow.append(noDegree)
        self.toWs.append(newRow)
        self.teacherTotal = 0
        self.reset()

