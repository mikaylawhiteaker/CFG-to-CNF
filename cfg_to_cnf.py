import csv

class converter():
    """docstring for converter."""
    def __init__(self):
        super(converter, self).__init__()
        grammar = {}

        # with open('level1.csv', newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         for i in row:
        #             print(i)

        with open('level1.csv', mode='r') as infile:
            reader = csv.reader(infile)
            with open('level1_new.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                grammar = {rows[0]:rows[1] for rows in reader}
        print(grammar)
        #self.newStartState(grammar)


    def newStartState(self, grammar):
        print("hello?")
        for row in grammar:
            print(row)

test = converter()
test.__init__()
