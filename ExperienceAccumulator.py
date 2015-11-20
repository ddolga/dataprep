from AccumulatorClass import Accumulator


class ExperienceAccumulator(Accumulator):
    map_exp_type = ["General", "Specialized", "Teaching"]
    map = ["<1", "1-5", "6-10", "11-15", "16-20", ">20"]

    headers = ["Year", "School Id", "Experience (Years)", "General", "Specialized", "Teaching"]

    def accumulateRow(self, row):

        for i in range(0, len(self.map_exp_type)):
            exp = row[self.startCol + i].value
            cat = self.calcCategory(exp)
            self.totals[i][cat] += row[2].value


    def calcCategory(self, exp):
        map = self.map
        v = None
        if (exp > 20):
            return len(map) - 1
        else:
            return exp % 5


    def initTotalsArray(self):
        self.totals = []
        for i in self.map_exp_type:
            row = []
            for h in self.map:
                row.append(0)
            self.totals.append(row)


    def appendRow(self, year, schoolId):
        for i in range(0, len(self.map)):
            newRow = []
            newRow.append(year)  # year
            newRow.append(schoolId)  # school id
            newRow.append(self.map[i])

            for r in range(0, len(self.map_exp_type)):
                newRow.append(self.totals[r][i])

            self.toWs.append(newRow)

        self.reset();
