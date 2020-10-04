#This is the unfolding program for general FSM

from z3 import *

import time
import sys

n = 3 # size of the input -- no of variables used in M

X = [Bool('x_%i' % i) for i in range(n)]
Y = [Bool('y_%i' % i) for i in range(n)]


print "printing the contents of X list:",
print X
print "printing the contents of Y list:",
print Y

print ""

#Input (M,P) is inline

#Boolean encoding of 3-bit ring counter M =(alpha_I,alpha_T)
alpha_I = And(X[2], And(Not(X[1]),Not(X[0])))
alpha_T = And(Y[2] == X[0], And(Y[1] == X[2], Y[0] == X[1]))

#Property for 3-bit ring counter
#P = Not(X[0])
P = And(Xor(X[2],Xor(X[1],X[0])),Not(And(X[2],And(X[1],X[0]))))

print "printing alpha_I:",
print alpha_I

print ""

print "printing alpha_T:",
print alpha_T

print ""

print "printing property P:",
print P

print ""

V = [] # List V holds the variables used in the runs -- (x_00,x_01,x_02),(x_10,x_11,x_12), etc.

Run = [] # List run holds the expressions run_0, run_1, etc.

Path = [] # List path holds the expressions path_0, path_1, etc.

L = [ Bool('x_%i%i' % (0,i)) for i in range(n) ]	
print "printing L:",
print L
print ""

for i in range(n):
	V.append(L[i])

#V.append(Bool('x_00'))
#V.append(Bool('x_01'))
#V.append(Bool('x_02'))

s = Solver()

run_0 = alpha_I
for i in range(n):
	run_0 = substitute(run_0,(X[i],V[i]))

#run_0 = substitute(alpha_I, (X[2],V[2]),(X[1],V[1]),(X[0],V[0]))

subp_0 = P
for i in range(n):
	subp_0 = substitute(subp_0,(X[i],V[i]))

#subp_0 = substitute(P, (X[2],V[2]),(X[1],V[1]),(X[0],V[0]))

print "printing run_0: ",
print run_0
print ""

print "printing subp_0: ",
print subp_0
print ""


Run.append(run_0)
Path.append(True)

s.add(run_0)
s.add(Not(subp_0))

result = s.check()

if result == sat:
	print "The input FSM is unsafe -- at the initial state"
	print "Printing a bad path of length 0"
	sys.exit("exiting")
else:
	print "All initial states are P-states -- safe for k = 0"
	print "Continuing for k = %i" %(0+1)
	print ""

s.reset()

time.sleep(5)

k = 1 # k is the length of the run

while k < pow(2,n):
#while True:
	L = [ Bool('x_%i%i' % (k,i)) for i in range(n) ]	
	print "printing L: ", L
	print ""

	for i in range(n):
		V.append(L[i])
	
	run_k = alpha_T
	for i in range(n):
		run_k = substitute(run_k, (X[i],V[n*(k-1)+i]),(Y[i],V[n*k+i]))
	run_k = And(Run[k-1],run_k)

	subp_k = P
	for i in range(n):
		subp_k = substitute(subp_k, (X[i],V[n*k+i]))

#	run_k = And(Run[k-1], substitute(alpha_T, (X[2],V[3*k-1]),(X[1],V[3*k-2]),(X[0],V[3*k-3]), (Y[2],V[3*k+2]),(Y[1],V[3*k+1]),(Y[0],V[3*k])))
#	subp_k = substitute(P, (X[2],V[3*k+2]),(X[1],V[3*k+1]),(X[0],V[3*k]))

	Run.append(run_k)

	print "printing run_k:", run_k
	print ""

	print "printing subp_k:", subp_k
	print ""

	s.add(run_k)
	s.add(Not(subp_k))

	result = s.check() # 

	if result == sat:
		print "The input FSM is unsafe -- for k = %i" %(k)
		sys.exit("exiting")
	else:
		print "All states at a distance %i are P-states -- safe for k = %i" %(k,k)
		print "Continuing for k = %i" %(k+1)
		print ""

	s.reset()

	
	k = k + 1

	time.sleep(5)

