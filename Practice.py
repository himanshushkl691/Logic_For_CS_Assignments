from z3 import *

s = Solver()

print('p1<=>(~p2 V p3))=>(~p1 => p2)')
s.push()
p1 = Bool('p1')
p2 = Bool('p2')
p3 = Bool('p3')
bool_formula = Implies((p1 == Or(Not(p2), p3)), Implies(Not(p1), p2))
s.add(Not(bool_formula))
if s.check() == unsat:
    print('Formula is Tautology.')
else:
    print('Formula is not Tautology.')
s.pop()

print('p1=>(p2 V p3))V(p1=>p2')
s.push()
bool_formula = Or(Implies(p1, Or(p2, p3)), Implies(p1, p2))
s.add(Not(bool_formula))
if s.check() == unsat:
    print('Formula is Tautology.')
else:
    print('Formula is not Tautology.')
s.pop()

print('(p=>q)^(q=>r)=>(p=>r)')
s.push()
p = Bool('p')
q = Bool('q')
r = Bool('r')
form1 = Implies(p, q)
form2 = Implies(q, r)
form3 = Implies(p, r)
bool_form = Implies(And(form1, form2), form3)
s.add(Not(bool_form))
if s.check() == unsat:
    print('Valid Formula')
else:
    print('Invalid Formula')
s.pop()

print('(p^q) = (~p V ~q)')
s.push()
lhs_form = And(p, q)
rhs_form = Not(Or(Not(p), Not(q)))
bool_form = (lhs_form == rhs_form)
s.add(Not(bool_form))
if s.check() == unsat:
    print('Valid Formula')
else:
    print('Invalid Formula')
s.pop()

print('{p V q, p => r,q => r} entails r')
s.push()
form1 = Or(p, q)
form2 = And(form1, Implies(p, r))
form3 = And(form2, Implies(q, r))
form4 = And(form3, Not(r))
s.add(form4)

if s.check() == unsat:
    print('Valid formula')
else:
    print('Invalid formula')
s.pop()

print('p=>(q=>~p)')
s.push()
conjecture = Implies(p, Implies(q, Not(p)))
print(conjecture)
conjecture = simplify(conjecture)
print(conjecture)
s.add(conjecture)
while s.check() == sat:
    m = s.model()
    print(m)
    extra = True
    for d in m.decls():
        if m[d] == True:
            extra = And(extra, Bool(d.name()))
        else:
            extra = And(extra, Not(Bool(d.name())))
        extra = simplify(extra)
    s.add(Not(extra))
s.pop()

s.push()
print('polynomial constraint')
x = Int('x')
y = Int('y')
s.add(x > 2, y < 10, x + 2 * y == 7)
s.check()
print(s.model())
s.pop()

X = IntVector('x', 5)
Y = RealVector('y', 5)
P = BoolVector('p', 5)
print(X)
print(Y)
print(P)
print([y**2 for y in Y])
print(Sum([y**2 for y in Y]))
