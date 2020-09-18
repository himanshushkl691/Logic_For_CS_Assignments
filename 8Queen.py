from z3 import *

solve_stack = Solver()
P = []
for i in range(8):
    P.append(Int('p_{}'.format(i + 1)))

# print(P)

for i in range(8):
    solve_stack.add(1 <= P[i], P[i] <= 8)
    for j in range(8):
        if i != j:
            solve_stack.add(P[i] != P[j])
            solve_stack.add(((P[i] - i) != (P[j] - j)))
            solve_stack.add(((P[i] + i) != (P[j] + j)))

# print(solve_stack)
solve_stack.check()
model = solve_stack.model()
print(model)
