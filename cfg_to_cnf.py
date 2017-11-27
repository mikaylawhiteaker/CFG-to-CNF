import csv

class converter():
    """docstring for converter."""
    def __init__(self):
        super(converter, self).__init__()

        reader = csv.reader(open('level2.csv'))
        grammar = {}
        for row in reader:
            key = row[0]
            grammar[key] = row[1:]
        #print(grammar)

        self.newStartState(grammar)


    def newStartState(self, grammar):
        grammar['S0'] = ['S']
        print(grammar)
        self.premoteEps(grammar)

    def premoteEps(self, grammar):
        #recursion
        e_present = False
        #base case is e only in start rule
        for k in grammar.keys():
            if (('e' in grammar.get(k)) and (k != 'S')):
                 e_present = True
        if(e_present):
            #print("premote")
            key_with_e = ''
            for k in grammar.keys():
                if (('e' in grammar.get(k)) and (k != 'S')):
                    terminals = grammar.get(k)
                    terminals.remove('e')
                    #print(terminals)
                    key_with_e = k
                    grammar[k] = terminals
            print("key_with_e")
            print(key_with_e)
            for key in grammar.keys():
                print("key")
                print(key)
                if(key_with_e != key):
                    terminals = grammar.get(key)[:]
                    new_terminals = grammar.get(key)[:]
                    for term in terminals:
                        if key_with_e in term:
                            print("term:")
                            print(term)
                            print("term k count:")
                            print(term.count(key_with_e))
                            for x in range(term.count(key_with_e)):
                                new_term = term.replace(key_with_e, '', x+1)
                                if new_term == '':
                                    new_term = 'e'
                                print("new term: ")
                                print(new_term)
                                print(new_terminals)
                                new_terminals.append(new_term)
                                print(new_terminals)
                            terminals.remove(term)
                            print(grammar)
                            grammar[key] = new_terminals
                            print(grammar)
            self.premoteEps(grammar)
        print(grammar)
        if( not e_present):
            print(grammar)
            self.ruleToRule(grammar)


    def ruleToRule(self, grammar):
        print("int rule to rule")
        print(grammar)


test = converter()
#test.__init__()
