from z3 import *


def atleast_one(formula):
    return Or(formula)


def atmost_one(formula):
    extra = True
    n = len(formula)
    for i in range(n):
        for j in range(i + 1, n):
            extra = And(extra, Or(Not(formula[i]), Not(formula[j])))
    return extra


def exactly_one(formula):
    return And(atmost_one(formula), atleast_one(formula))


solver_stack = Solver()
C = []
D = []
E = []
for i in range(15):
    D.append([])
for i in range(15):
    E.append([])

for i in range(8):
    for j in range(8):
        C.append(Bool('Q_{}_{}'.format(i + 1, j + 1)))
        D[(i + j)].append(Bool('Q_{}_{}'.format(i + 1, j + 1)))
        E[(i - j) + 7].append(Bool('Q_{}_{}'.format(i + 1, j + 1)))
# print(C)
# for i in range(15):
#     print(D[i])
# for i in range(15):
#     print(E[i])

for i in range(15):
    solver_stack.add(atmost_one(D[i]))
    solver_stack.add(atmost_one(E[i]))

for i in range(8):
    solver_stack.add(exactly_one(C[8 * i: 8 * i + 8]))
    tmp = []
    for j in range(8):
        tmp.append(C[i + 8 * j])
    solver_stack.add(exactly_one(tmp))

i = 0
while solver_stack.check() == sat:
    model = solver_stack.model()
    extra = True
    print('[', end=' ')
    for d in model.decls():
        if model[d] == True:
            print(d.name(), ':', model[d], ' ', end=' ')
            extra = And(extra, Bool(d.name()))
        else:
            extra = And(extra, Not(Bool(d.name())))
        extra = simplify(extra)
    print(']')
    solver_stack.add(Not(extra))
    i = i + 1

print('Total solution: {}'.format(i))
