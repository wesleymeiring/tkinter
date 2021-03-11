class Candidate:
    title = 'Mr.'
    name = ''
    surname = ''
    scores = []
    average = 0

    def __init__(self, name, surname, scores, gender):
        self.name = name
        self.surname = surname
        self.scores = scores
        self.gender = gender
        # call functions
        self.setAverage()
        self.setLowest()
        self.setHighest()

    def printDetails(self):
        print("\n== Candidate Details ==")
        print("Name: \t\t {} {}".format(self.gender_text(), self.name))
        print("Surname: \t {}".format(self.surname))
        print("Scores: \t {}".format(self.scores))
        print("")
        print("Average: \t {:.2f}".format(self.average))
        print("Lowest: \t {}".format(self.lowest))
        print("Highest: \t {}".format(self.highest))
        print("-------------------------")

    def setAverage(self):
        total = 0
        count = 0
        for score in self.scores:
            total += score
            count += 1
            self.average = (total / count)

    def setLowest(self):
        self.lowest = min(self.scores)

    def setHighest(self):
        self.highest = max(self.scores)

    def gender_text(self):
        if self.gender == "male":
            return "Mr"
        if self.gender == "female":
            return "Mrs"


candidate1 = Candidate("wesley", "meiring", [10, 20, 80], "male")
candidate1.printDetails()

candidate3 = Candidate("Michaela", "Earle", [15, 18, 92], "female")
candidate3.printDetails()

candidate3 = Candidate("Hendrik", "Prinsloo", [50, 80, 99], "male")
candidate3.printDetails()
