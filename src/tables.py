import itertools

class Row:
    def __init__(self, variableValues, expressionValue):
        self.variableValues = variableValues
        self.expressionValue = expressionValue

def getStatement():
    return input('Enter your statement. Be sure to use legal Python boolean expression syntax, using parentheses as needed: ')


def getVarName():
    name = input("Enter the names of your variables seperated by a space. (7 is the maximum number of variables; 1 is the minimum number of variables): ").split()
    while len(name) == 0 or len(name) > 7:
        name = input("Enter the names of your variables seperated by a space. (7 is the maximum number of variables; 1 is the minimum number of variables): ").split()       
    return name


def checkStatement(nameList, statement):
    temp = statement.lower()
    if temp.count("(") != temp.count(")"):
        return False
    temp = temp.replace("and", "").replace("or", "").replace("not", "").replace(" ", "").replace("(", "").replace(")","")
    for name in nameList:
        temp = temp.replace(name, "")
    if len(temp)>0:
        return False
    return True


def getTable(nameList, statement):
    evaluatedExpressionList = []
    variableValueList = itertools.product([False, True], repeat=len(nameList))
    for row in variableValueList:
        for i in range(len(nameList)):
            exec(nameList[i] + "= row[i]")
        fin = Row(row, eval(statement))
        evaluatedExpressionList.append(fin)
    return evaluatedExpressionList


    
def formatTable(nameList, statement, evaluatedExpressionList):
    table = ""
    for name in nameList:
        table += " " + name + " " * (7-len(name)-1) + "|"
    table += " " + statement + "\n"
    sep = "\n" + "=" * len(table) + "\n"
    for row in evaluatedExpressionList:
        for truth in row.variableValues:
            table += " " + str(truth) + " " * (7-len(str(truth))-1) + "|"
        table += " " + str(row.expressionValue) + "\n"
    
    return sep+table
