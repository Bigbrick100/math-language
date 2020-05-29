from Token import *
from char import getCharType


class Parcer:
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile

        self.letterBuffer = []
        self.digitBuffer = []
        self.tokenList = []

        self.mode = "letter"
        self.currentBuffer = self.letterBuffer

    def parce(self):
        with open(self.sourceFile, 'r') as i:
            lines = i.readlines()
            for x, line in enumerate(lines):
                for y, char in enumerate(line):
                    self.handleInput(char, getCharType(char))
        self.endFile()
        self.floatizeDigits()

    def handleInput(self, char, charType):
        # handles chars that belong to current reader mode
        if (self.mode == charType):
            self.currentBuffer.append(char)
            return

        # handles switch to letter mode
        elif (charType == "letter"):
            if (len(self.digitBuffer) > 0):
                self.tokenList.append(
                    Token("digit", simplify(self.digitBuffer)))
                self.digitBuffer.clear()

            self.setMode("letter")

        # handles switch to digit mode
        elif (charType == "digit"):
            if (len(self.letterBuffer) > 0):
                self.tokenList.append(
                    Token("letter", simplify(self.letterBuffer)))
                self.letterBuffer.clear()

            self.setMode("digit")

        # handles operators [(,),*,/,etc]
        elif (charType == "operator" or charType == "leftPara" or charType == "rightPara"):
            if (len(self.currentBuffer) > 0):
                self.tokenList.append(
                    Token(self.mode, simplify(self.currentBuffer)))
                self.currentBuffer.clear()

            self.tokenList.append(Token(charType, char))
            return

        # handles delemeter (|n or EOF or ,)
        elif (charType == "delemeter" or charType == "comma"):
            if (len(self.currentBuffer) > 0):
                self.tokenList.append(
                    Token(self.mode, simplify(self.currentBuffer)))
                self.currentBuffer.clear()

            self.tokenList.append(Token(charType, ""))
            return

        elif (charType == "space"):
            return

        self.handleInput(char, charType)

    def setMode(self, mode):
        self.mode = mode

        if (mode == "letter"):
            self.currentBuffer = self.letterBuffer
        elif (mode == "digit"):
            self.currentBuffer = self.digitBuffer

    def floatizeDigits(self):
        for token in self.tokenList:
            if(token.type == "digit"):
                token.value = float(token.value)

    def endFile(self):
        self.handleInput("", "delemeter")

    def print(self):
        for token in self.tokenList:
            token.print()


def simplify(c):
    r = ''
    for x in c:
        r += x
    return r
