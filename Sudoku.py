from z3 import *

"""Encoding: A_i_j_k is True if A[i][j] == k. Else False"""


def atleast_one(formula):
    return Or(formula)


def atmost_one(formula):
    extra = True
    n = len(formula)
    for i in range(n):
        for j in range(i + 1, n):
            extra = And(extra, Or(Not(formula[i]), Not(formula[j])))
            extra = simplify(extra)
    return extra


def exactly_one(formula):
    return And(atmost_one(formula), atleast_one(formula))


solve_stack = Solver()

A = []
Column_Formula = []
for i in range(9):
    Column_Formula.append([])
    for j in range(9):
        Column_Formula[i].append([])
for i in range(9):  # row
    for k in range(9):  # digit
        tmp = []
        for j in range(9):  # column
            form = Bool('A_{}_{}_{}'.format(i + 1, j + 1, k + 1))
            Column_Formula[k][j].append(form)
            tmp.append(form)
        A.append(tmp)
        solve_stack.add(exactly_one(tmp))

for j in range(9):  # column
    for k in range(9):  # digit
        solve_stack.add(exactly_one(Column_Formula[k][j]))

for i in range(9):
    for j in range(9):
        tmp = []
        for k in range(9):
            form = Bool('A_{}_{}_{}'.format(i + 1, j + 1, k + 1))
            tmp.append(form)
        solve_stack.add(exactly_one(tmp))

for i in range(0, 9, 3):  # row
    for j in range(0, 9, 3):
        for m in range(9):
            tmp = []
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    form = Bool('A_{}_{}_{}'.format(k + 1, l + 1, m + 1))
                    tmp.append(form)
            solve_stack.add(exactly_one(tmp))
# print(A)
# print(Column_Formula)
# print(solve_stack)

solve_stack.check()
model = solve_stack.model()

print('[', end=' ')
for d in model.decls():
    if model[d] == True:
        print(d.name(), ':', model[d], ' ', end=' ')
print(']')
