import re


def getCharType(c):
    if (isLetter(c)):
        return "letter"
    elif (isDigit(c)):
        return "digit"
    elif (isDelimeter(c)):
        return "delemeter"
    elif (isSpace(c)):
        return "space"
    elif (isComma(c)):
        return "comma"
    elif (isOperator(c)):
        return "operator"
    elif (isLeftParenthesis(c)):
        return "leftPara"
    elif (isRightParenthesis(c)):
        return "rightPara"


def isEnd(c):
    list = re.findall(";", c)
    if len(list) > 0:
        return True
    else:
        return False


def isDelimeter(c):
    list = re.findall("\n", c)
    if len(list) > 0:
        return True
    else:
        return False


def isSpace(c):
    list = re.findall("\s", c)
    if len(list) > 0:
        return True
    else:
        return False


def isComma(c):
    list = re.findall(",", c)
    if len(list) > 0:
        return True
    else:
        return False


def isDigit(c):
    list = re.findall("\d", c)
    if len(list) > 0:
        return True
    else:
        return False


def isLetter(c):
    list = re.findall("[a-zA-Z]", c)
    if len(list) > 0:
        return True
    else:
        return False


def isOperator(c):
    list = re.findall("\%|\*|\/|\+|\-|\^|\=", c)
    if len(list) > 0:
        return True
    else:
        return False


def isLeftParenthesis(c):
    list = re.findall("\(", c)
    if len(list) > 0:
        return True
    else:
        return False


def isRightParenthesis(c):
    list = re.findall("\)", c)
    if len(list) > 0:
        return True
    else:
        return False
