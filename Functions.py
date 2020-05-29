import math
from Errors import Error

savedFunctions = {"t": 10}


class Function:
    def __init__(self):
        self.name = None
        self.term = None
        self.terms = []
        self.requiredVars = []

        self.constant = 1
        self.power = 1

    def evaluateAt(self, values):
        if(len(self.terms) > 0):
            if(self.term):
                sum = 0
                for term in self.terms:
                    sum += term.evaluateAt(values)

                return self.constant*(sum**self.power)
            else:
                product = 1
                for term in self.terms:
                    product *= term.evaluateAt(values)
                return self.constant * product
        else:
            value = values[self.requiredVars[0]]
            return self.constant*(value**self.power)


class trigFunction(Function):
    def __init__(self, func):
        super().__init__()
        self.innerFunc = func

    def evaluateAt(self, values):
        sum = 0
        for term in self.terms:
            sum += term.evaluateAt(values)

        return self.innerFunc(sum)
