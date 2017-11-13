import csv

class converter():
    """docstring for converter."""
    def __init__(self):
        super(converter, self).__init__()

        reader = csv.reader(open('level1.csv'))
        grammar = {}
        for row in reader:
            key = row[0]
            grammar[key] = row[1:]
        print(grammar)

        self.newStartState(grammar)


    def newStartState(self, grammar):
        grammar['S0'] = ['S']
        print(grammar)
        self.premoteEps(self, grammar)

    def premoteEps(self, grammar):
        print("hmm...")

test = converter()
#test.__init__()
