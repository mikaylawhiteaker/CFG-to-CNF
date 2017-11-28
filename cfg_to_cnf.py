import csv
import re

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
                    #print(grammar[k])
            #print("key_with_e")
            #print(key_with_e)
            for key in grammar.keys():
                #print("key")
                #print(key)
                if(key_with_e != key):
                    terminals = grammar.get(key)[:]
                    new_terminals = grammar.get(key)[:]
                    for term in terminals:
                        if key_with_e in term:
                            #print("term:")
                            #print(term)
                            #print("term k count:")
                            #print(term.count(key_with_e))
                            new_term = term.replace(key_with_e, '')
                            if new_term not in new_terminals and term.count(key_with_e) > 1:
                                new_terminals.append(new_term)
                            for m in re.finditer(key_with_e, term):
                                new_term = term[:m.start()] + term[m.start()+1:]
                                if new_term == '':
                                    new_term = 'e'
                                #print("new term: ")
                                #print(new_term)
                                #print(new_terminals)
                                new_terminals.append(new_term)
                                #print(new_terminals)
                            terminals.remove(term)
                            #print(grammar)
                            grammar[key] = new_terminals
                            #print(grammar)
            self.premoteEps(grammar)
        #print(grammar)
        if( not e_present):
            #print(grammar)
            #self.removeRuleToRule(grammar)
            self.copyToNewStart(grammar)

    #def removeRuletoRule(self, grammar):
        # S-> S
        #self.copyToNewStart(grammar)

    def copyToNewStart(self, grammar):
        #s0 -> S
        print("copy new start rule")
        for key in grammar.keys():
            if(key == 'S'):
                terms = grammar.get(key)
                #print(terms)
                #print(grammar)
                grammar['S0'] = terms
                #print (grammar)
        #self.ruleToRuleToTerm(grammer)

    def ruleToRuleToTerm(self, grammar):
        print("int rule to rule")
        print(grammar)
        #for key in grammar.keys():
            #for term in grammar.get(key):
                #if(len(term) == 1):
                    #if()


test = converter()
#test.__init__()
