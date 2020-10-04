from z3 import *


X = []
Y = []

X.append(Bool('x_0'))
X.append(Bool('x_1'))
X.append(Bool('x_2'))

Y.append(Bool('y_0'))
Y.append(Bool('y_1'))
Y.append(Bool('y_2'))

#aI = expr('aI')
#aT = expr('aT')

alpha_I = And(X[2], And(Not(X[1]), Not(X[0])))
alpha_T = And(Y[2] == X[0], And(Y[1] == X[2], Y[0] == X[1]))

P = Not(X[0])

print(alpha_I)
print(alpha_T)
print(P)


V = []

V.append(Bool('x_00'))
V.append(Bool('x_01'))
V.append(Bool('x_02'))

V.append(Bool('x_10'))
V.append(Bool('x_11'))
V.append(Bool('x_12'))

V.append(Bool('x_20'))
V.append(Bool('x_21'))
V.append(Bool('x_22'))

V.append(Bool('x_30'))
V.append(Bool('x_31'))
V.append(Bool('x_32'))

s = Solver()

run_0 = substitute(alpha_I, (X[2], V[2]), (X[1], V[1]), (X[0], V[0]))
subp_0 = substitute(P, (X[2], V[2]), (X[1], V[1]), (X[0], V[0]))
print(run_0)
print(subp_0)


s.add(run_0)
s.add(Not(subp_0))

print(s.check())  # returns unsat as P holds for inital state (1,0,0)

s.reset()

run_1 = And(run_0, substitute(
    alpha_T, (X[2], V[2]), (X[1], V[1]), (X[0], V[0]), (Y[2], V[5]), (Y[1], V[4]), (Y[0], V[3])))
subp_1 = substitute(P, (X[2], V[5]), (X[1], V[4]), (X[0], V[3]))

print(run_1)
print(subp_1)

s.add(run_1)
s.add(Not(subp_1))

print(s.check())  # returns unsat as P holds for inital state (0,1,0)


s.reset()

run_2 = And(run_1, substitute(
    alpha_T, (X[2], V[5]), (X[1], V[4]), (X[0], V[3]), (Y[2], V[8]), (Y[1], V[7]), (Y[0], V[6])))
subp_2 = substitute(P, (X[2], V[8]), (X[1], V[7]), (X[0], V[6]))

print(run_2)
print(subp_2)

s.add(run_2)
s.add(Not(subp_2))

print(s.check())  # returns sat

print(s.model())
