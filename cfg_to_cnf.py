import csv
import re
import string
import random


class converter():
    """docstring for converter."""
    def __init__(self):
        super(converter, self).__init__()

        reader = csv.reader(open('level1.csv'))
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
            self.removeRuletoRule(grammar)
            #self.copyToNewStart(grammar)

    def removeRuletoRule(self, grammar):
        # S-> S
        #print(grammar)
        for key in grammar.keys():
            if (key in grammar.get(key)):
                #print(key)
                variables = grammar.get(key)
                variables.remove(key)
                #print(grammar)

        self.copyToNewStart(grammar)

    def copyToNewStart(self, grammar):
        #s0 -> S
        #print("copy new start rule")
        for key in grammar.keys():
            if(key == 'S'):
                terms = grammar.get(key)
                #print(terms)
                #print(grammar)
                grammar['S0'] = terms[:]

                if('e' in terms):
                    grammar.get(key).remove('e')
                #print (grammar)
        self.ruleToRuleToTerm(grammar)

    def ruleToRuleToTerm(self, grammar):
        #print("int rule to rule")
        #print(grammar)
        for key in grammar.keys():
            #print("key: " + key)
            for term in grammar.get(key):
                #print("term: " + term)
                if len(term) == 1 and term.isupper():
                    grammar.get(key).remove(term)
                    for t in grammar.get(term):
                        grammar.get(key).insert(0, t)
        #print(grammar)
        self.threeOrMoreTerm(grammar)

    def threeOrMoreTerm(self, grammar):
        print("in threeOrMoreTerm")
        print(grammar)
        lessThanThree = True
        for key, value in grammar.items():
            for term in value:
                if(len(term) >= 3):
                    lessThanThree = False
                    break
        if lessThanThree:
            print("all less than three")
            self.ruleToOnlyTerminal(grammar)
        if not lessThanThree:
            print("split up")
            self.splitUpterm(grammar)
            self.threeOrMoreTerm(grammar)

    def splitUpterm(self, grammar):
        for key in grammar.keys():
            for term in grammar.get(key):
                if len(term) >= 3:
                    first = term[0:1]
                    if self.checkForRule(grammar, term[1:]) is not None:
                        newRule = self.checkForRule(grammar, term[1:])
                        grammar.get(key).remove(term)
                        grammar.get(key).append(first+newRule)
                    else:
                        newRule = self.getNewRule(grammar)
                        grammar[newRule] = [term[1:]]
                        grammar.get(key).remove(term)
                        grammar.get(key).append(first+newRule)
                    return

    def checkForRule(self, grammar, term):
        for key, values in grammar.items():
            if len(values) == 1 and term in values:
                return key
        return None

    def getNewRule(self, grammar):
        char = random.choice(string.ascii_uppercase)
        #print("char:")
        #print(char)
        if char not in grammar:
            #print("HEY!:" +char)
            return char
        else:
            self.getNewRule(grammar)
            #char = random.choice(string.ascii_uppercase)

        def removeRuletoTerm(self,grammar):
            #A -> aB into A -> UB AND U -> a
            tempTerm = ''
            newVariable = ''
            for key in grammar.keys():
                for term in grammar.get(key):
                    if len(term) == 2 and (term[0].islower() or term[1].islower()):
                        if(term[0].lower()):
                            tempTerm = term[0]
                            newVariable = 'U' #USE RANDOM LETTER GENERATOR
                            grammar.get(key).remove(term)
                            term = term.replace(term[0], newVariable)
                            grammar.get(key).append(term)
                            print(grammar)
                        if(term[1].islower()):
                            tempTerm = term[1]
                            newVariable = 'U' #USE RANDOM LETTER GENERATOR
                            grammar.get(key).remove(term)
                            term = term.replace(term[1], newVariable)
                            grammar.get(key).append(term)
            grammar[newVariable] = [tempTerm]
            print(grammar)
            self.ruleToOnlyTerminal(grammar)

    def ruleToOnlyTerminal(self, grammar):
        print("in finall function")
        print(grammar)


test = converter()
#test.__init__()
