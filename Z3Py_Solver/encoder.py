from z3 import *

NOT = '~'
OR = '|'
AND = '&'
XOR = '^'
IMPLIES = '%'
EQUIVALENCE = '#'


class Node:
    def __init__(self, operator, str):
        self.operator = operator
        self.str = str
        self.left = None
        self.right = None

    def setLeftChild(self, child):
        self.left = child

    def setRightChild(self, child):
        self.right = child

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def isOperator(self):
        return (self.operator == 1)

    def getLiteral(self):
        return (self.str)

    def printPreorder(self):
        if self == None:
            return
        print('[' + str(self.operator) + ', ' + self.str + '] ', end=' ')
        if self.left != None:
            self.left.printPreorder()
        if self.right != None:
            self.right.printPreorder()

    def printInorder(self):
        if self == None:
            return
        if self.left != None:
            self.left.printInorder()
        print('[' + str(self.operator) + ', ' + self.str + '] ', end=' ')
        if self.right != None:
            self.right.printInorder()

    def printPostorder(self):
        if self == None:
            return
        if self.left != None:
            self.left.printPostorder()
        if self.right != None:
            self.right.printPostorder()
        print('[' + str(self.operator) + ', ' + self.str + '] ', end=' ')


def getOp(i, arr):
    bal = 0
    n = len(arr)
    while i < n:
        if arr[i] == '(':
            bal += 1
        elif arr[i] == ')':
            bal -= 1
        if bal == 0:
            return (i + 1)
        i += 1


def isLiteral(i, j, arr):
    open = 0
    close = 0
    idx = i
    while idx <= j:
        if arr[idx] == '(':
            open += 1
        if arr[idx] == ')':
            close += 1
        idx += 1
    return (open == 1 and close == 1)


def createTree(i, j, arr):
    if i > j:
        return None
    if isLiteral(i, j, arr):
        return Node(1, arr[i + 1: j])
    if arr[i + 1] == NOT:
        root = Node(0, NOT)
        root.setLeftChild(createTree(i + 2, j - 1, arr))
        return root
    else:
        mid = getOp(i + 1, arr)
        # print('[' + str(mid) + ', ' + str(i) + ', ' + str(j) + ']')
        root = Node(0, arr[mid])
        root.setLeftChild(createTree(i + 1, mid - 1, arr))
        root.setRightChild(createTree(mid + 1, j - 1, arr))
        return root


def xorHelper(formula1, formula2):
    firstTerm = Or(Not(formula1), Not(formula2))
    secondTerm = Or(formula1, formula2)
    return And(firstTerm, secondTerm)


def encodeFormulaToZ3(root):
    if root == None:
        return None
    if root.isOperator() == 1:
        return Bool(root.getLiteral())
    else:
        leftFormula = encodeFormulaToZ3(root.getLeftChild())
        rightFormula = encodeFormulaToZ3(root.getRightChild())
        literal = root.getLiteral()
        if literal == NOT:  # contains only left child
            return Not(leftFormula)
        elif literal == AND:
            return And(leftFormula, rightFormula)
        elif literal == OR:
            return Or(leftFormula, rightFormula)
        elif literal == XOR:
            return xorHelper(leftFormula, rightFormula)
        elif literal == IMPLIES:
            return Implies(leftFormula, rightFormula)
        elif literal == EQUIVALENCE:
            return (leftFormula == rightFormula)


formula = str(input())
n = len(formula)
root = createTree(0, n - 1, formula)
# root.printInorder()
# print()
# root.printPostorder()
# print()
# root.printPreorder()
# print()
boolform = encodeFormulaToZ3(root)
print(boolform)
s = Solver()
s.add(boolform)
print(s.check())
# print(s.model())
