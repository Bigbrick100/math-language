# TODO Fix handleParas

from Functions import Function, savedFunctions
from Token import Token


class Executor:
    def __init__(self, parser):
        self.parser = parser
        self.tokenBuffer = []

        self.mode = "arithmetic"

        self.currentDigit = 0
        self.currentOperator = None

    def execute(self):
        for token in self.parser.tokenList:
            if(self.mode == "arithmetic"):
                if(token.type != "delemeter"):
                    self.tokenBuffer.append(token)
                else:
                    tokenList = self.handleParas(self.tokenBuffer)
                    print(self.getValue(tokenList))
                    self.tokenBuffer = []

    def handleParas(self, tokenList):
        paraOffset = 0
        paraPositions = []
        x = 0
        for token in tokenList:
            if(token.type == "leftPara"):
                paraPositions.append(x)
                paraOffset += 1
            elif(token.type == "rightPara"):
                paraPositions.append(x)
                paraOffset -= 1

            x += 1

        if(paraOffset != 0):
            print("offset error")
        elif(len(paraPositions) % 2 != 0):
            print("even error")

        while(len(paraPositions) > 0):
            middle = int(len(paraPositions)/2-1)
            leftPara = paraPositions[middle]
            rightPara = paraPositions[middle+1]

            value = self.getValue(tokenList[leftPara+1:rightPara])
            del tokenList[leftPara:rightPara+1]
            del paraPositions[middle:middle+2]
            tokenList.insert(leftPara, Token("digit", value))

        return tokenList

    # takes a token list without parenthesis and return the value
    def getValue(self, tokenList):

        # handles ^ arithmetic
        pos = 0
        while(pos < len(tokenList)):
            if(tokenList[pos].value == "^"):
                if(tokenList[pos+1].value == "-"):
                    tokenList[pos+2].value = -tokenList[pos+2].value
                    del tokenList[pos+1:pos+2]

                leftVal = tokenList[pos-1].value
                rightVal = tokenList[pos+1].value

                value = leftVal**rightVal

                del tokenList[pos-1:pos+2]
                tokenList.insert(pos-1, Token("digit", value))
                pos -= 1
            pos += 1

        # handles * and / arithmetic
        pos = 0
        while(pos < len(tokenList)):
            if(tokenList[pos].value == "*" or tokenList[pos].value == "/"):
                if(tokenList[pos+1].value == "-"):
                    tokenList[pos+2].value = -tokenList[pos+2].value
                    del tokenList[pos+1:pos+2]

                leftVal = tokenList[pos-1].value
                rightVal = tokenList[pos+1].value

                if(tokenList[pos].value == "*"):
                    value = leftVal*rightVal
                else:
                    value = leftVal/rightVal

                del tokenList[pos-1:pos+2]
                tokenList.insert(pos-1, Token("digit", value))
                pos -= 1
            pos += 1

        # handles + and - arithmetic
        pos = 0
        while(pos < len(tokenList)):
            if(tokenList[pos].value == "+" or tokenList[pos].value == "-"):
                if(tokenList[pos+1].value == "-"):
                    tokenList[pos+2].value = -tokenList[pos+2].value
                    del tokenList[pos+1:pos+2]

                leftVal = tokenList[pos-1].value
                rightVal = tokenList[pos+1].value

                if(tokenList[pos].value == "+"):
                    value = leftVal+rightVal
                else:
                    value = leftVal-rightVal

                del tokenList[pos-1:pos+2]
                tokenList.insert(pos-1, Token("digit", value))
                pos -= 1
            pos += 1

        return tokenList[0].value
