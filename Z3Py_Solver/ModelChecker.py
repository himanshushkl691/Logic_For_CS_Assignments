from z3 import *

NOT = '~'
AND = '&'
OR = '|'
XOR = '^'
IMPLIES = '%'
EQUIVALENCE = '#'
precedence = {'~': 5, '&': 4, '|': 3, '^': 2, '%': 1, '#': 0}

"""TREE DEFINITION"""


class Node:
    def __init__(self, operator, str):
        self.operator = operator
        self.str = str
        self.left = None
        self.right = None

    def __repr__(self):
        return ('[' + str(self.operator) + ', ' + self.str + ']')

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


"""TREE DEFINITION ENDS HERE"""

"""RECURSION BASED"""
"""Converts textual formula to tree"""


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


def createTreeRecursive(i, j, arr):
    if i > j:
        return None
    if isLiteral(i, j, arr):
        return Node(1, arr[i + 1: j])
    if arr[i + 1] == NOT:
        root = Node(0, NOT)
        root.setLeftChild(createTreeRecursive(i + 2, j - 1, arr))
        return (root if (root.getLeftChild() != None) else None)
    else:
        mid = getOp(i + 1, arr)
        if mid >= j:
            return None
        # print('[' + str(mid) + ', ' + str(i) + ', ' + str(j) + ']')
        root = Node(0, arr[mid])
        root.setLeftChild(createTreeRecursive(i + 1, mid - 1, arr))
        root.setRightChild(createTreeRecursive(mid + 1, j - 1, arr))
        return (root if (root.getLeftChild() != None and root.getRightChild() != None) else None)


"""RECURSION BASED ENDS HERE"""


"""STACK BASED"""
"""Prefer this.Converts textual formula to tree based on precedence if paranthesis not present
otherwise parathesis precedence is followed"""


def isOperator(char):
    return (char == NOT or char == AND or char == OR or char == XOR or char == IMPLIES or char == EQUIVALENCE)


def createTreeIterative(str):
    nodeStack = []
    operatorStack = []
    n = len(str)
    i = 0
    while i < n:
        if str[i] == '(':
            operatorStack.append(str[i])
        elif str[i] == ')':
            if len(operatorStack) == 0:
                print('Invalid Expression')
                exit(1)
            while len(operatorStack) > 0 and isOperator(operatorStack[len(operatorStack) - 1]):
                op = operatorStack.pop()
                root = Node(0, op)
                if op != NOT:
                    rightSub = nodeStack.pop()
                    root.setRightChild(rightSub)
                leftSub = nodeStack.pop()
                root.setLeftChild(leftSub)
                nodeStack.append(root)
            if len(operatorStack) == 0 or operatorStack[len(operatorStack) - 1] != '(':
                print('Invalid Expression')
                exit(1)
            else:
                operatorStack.pop()
        elif isOperator(str[i]):
            while len(operatorStack) > 0 and isOperator(operatorStack[len(operatorStack) - 1]) and precedence[str[i]] <= precedence[operatorStack[len(operatorStack) - 1]]:
                op = operatorStack.pop()
                root = Node(0, op)
                if op != NOT:
                    rightSub = nodeStack.pop()
                    root.setRightChild(rightSub)
                leftSub = nodeStack.pop()
                root.setLeftChild(leftSub)
                nodeStack.append(root)
            operatorStack.append(str[i])
        elif str[i].isalnum():
            j = i
            lit = ''
            while j < n and str[j].isalnum():
                lit += str[j]
                j += 1
            nodeStack.append(Node(1, lit))
            i = j - 1
        else:
            print('Invalid Expression')
            exit(1)
        # print(nodeStack)
        # print(operatorStack)
        i += 1
    if len(nodeStack) != 1 and len(operatorStack) != 0:
        return None
    return nodeStack.pop()


"""STACK BASED TREE CONVERSION ENDS HERE"""

"""ENCODES TREE REPRESENTATION OF FORMULA TO Z3Py FORMAT"""


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
            return simplify(Not(leftFormula))
        elif literal == AND:
            return simplify(And(leftFormula, rightFormula))
        elif literal == OR:
            return simplify(Or(leftFormula, rightFormula))
        elif literal == XOR:
            return simplify(Xor(leftFormula, rightFormula))
        elif literal == IMPLIES:
            return Implies(leftFormula, rightFormula)
        elif literal == EQUIVALENCE:
            return (leftFormula == rightFormula)


"""ENDS HERE"""

"""si = {x_i_0,x_i_1,x_i_2,x_i_3,...,x_i_n-1}
sj = {x_j_0',x_j_1',x_j_2',x_j_3',...,x_j_n-1'}
n is number of boolean variables
returns boolean formula representing si==sj"""


def equalState(i, j, n):
    tmp = []
    for k in range(n):
        firstLiteral = Bool('x_' + str(i) + '_' + str(k))
        secondLiteral = Bool('x_' + str(j) + '_' + str(k))
        tmp.append((firstLiteral == secondLiteral))
    return And(tmp)


def checkModel(n, alphaI, alphaT, P):
    alphaI = encodeFormulaToZ3(createTreeIterative(alphaI))
    alphaT = encodeFormulaToZ3(createTreeIterative(alphaT))
    P = encodeFormulaToZ3(createTreeIterative(P))
    # print(alphaI)
    # print(alphaT)
    # print(P)
    # 0th run and sub_P is P substituted with (xi -> x_0_i)
    run = alphaI
    sub_P = P
    for i in range(n):
        tmp1 = Bool('x' + str(i))
        tmp2 = Bool('x_0_' + str(i))
        run = substitute(run, (tmp1, tmp2))
        sub_P = substitute(sub_P, (tmp1, tmp2))
    initial = run  # Initial(s0)
    loopFree = True     # no loop for zero length
    RUNS = 0
    solve_stack = Solver()
    while True:
        solve_stack.reset()
        # check for loop
        solve_stack.add(initial)
        solve_stack.add(loopFree)
        if solve_stack.check() == unsat:
            print('Model is P-safe')
            return
        solve_stack.reset()
        solve_stack.add(loopFree)
        solve_stack.add(Not(sub_P))
        if solve_stack.check() == unsat:
            print('Model is P-safe')
            return
        solve_stack.reset()
        # check ith run
        solve_stack.add(run)
        solve_stack.add(Not(sub_P))
        res = solve_stack.check()
        if res == sat:
            print('Model is not P-safe on run:')
            model = solve_stack.model()
            literals = []
            hash = {}
            for d in model.decls():
                literals.append(d.name())
                hash[d.name()] = model[d]
            literals.sort()
            for i in range(0, len(literals), n):
                print('(', end=' ')
                j = i
                while j < i + n:
                    if j == i + n - 1:
                        print('1' if hash[literals[j]] else '0', end=' )')
                    else:
                        print('1' if hash[literals[j]] else '0', end=', ')
                    j += 1
                if i < len(literals) - n - 1:
                    print(' --> ', end='')
                else:
                    print()
            return
        solve_stack.reset()
        RUNS += 1
        sub_alphaT = alphaT
        sub_P = P
        for j in range(n):
            tmpx = Bool('x' + str(j))
            tmpy = Bool('y' + str(j))
            tmpx_ = Bool('x_' + str(RUNS - 1) + '_' + str(j))
            tmpX_ = Bool('x_' + str(RUNS) + '_' + str(j))
            sub_alphaT = substitute(sub_alphaT, (tmpx, tmpx_), (tmpy, tmpX_))
            sub_P = substitute(sub_P, (tmpx, tmpX_))
        notEqualStates = []
        for j in range(RUNS):
            notEqualStates.append(Not(equalState(j, RUNS, n)))
        loopFree = And(loopFree, sub_alphaT)
        loopFree = And(loopFree, And(notEqualStates))
        run = And(run, sub_alphaT)


File = open('input.txt', 'r')
line = File.readline()
while line:
    n = int(line.strip())
    if n < 1:
        print('Invalid number of Boolean variables, provide n>=1')
        exit(1)
    alphaI = str(File.readline().strip())
    alphaT = str(File.readline().strip())
    P = str(File.readline().strip())
    print('*')
    checkModel(n, alphaI, alphaT, P)
    line = File.readline()
File.close()
