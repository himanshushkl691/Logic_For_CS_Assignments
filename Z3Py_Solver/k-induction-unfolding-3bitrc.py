#This is the unfolding program for 3-bit ring counter

from z3 import *

import time
import sys

X = []
Y = []

X.append(Bool('x_0'))
X.append(Bool('x_1'))
X.append(Bool('x_2'))

Y.append(Bool('y_0'))
Y.append(Bool('y_1'))
Y.append(Bool('y_2'))

#3-bit counter
alpha_I = And(X[2], And(Not(X[1]),Not(X[0])))
alpha_T = And(Y[2] == X[0], And(Y[1] == X[2], Y[0] == X[1]))

#P = Not(X[0]) # does not hold for k=2
P = And(Xor(X[2],Xor(X[1],X[0])),Not(And(X[2],And(X[1],X[0])))) # holds for all k

print "alpha_I: ", alpha_I
print "alpha_T: ", alpha_T
print "P: ", P
print ""
V = [] # List V holds the variables used in the runs -- (x_00,x_01,x_02),(x_10,x_11,x_12), etc.

Run = [] # List run holds the expressions run_0, run_1, etc.

Path = [] # List path holds the expressions path_0, path_1, etc.

V.append(Bool('x_00'))
V.append(Bool('x_01'))
V.append(Bool('x_02'))

s = Solver()

run_0 = substitute(alpha_I, (X[2],V[2]),(X[1],V[1]),(X[0],V[0]))
subp_0 = substitute(P, (X[2],V[2]),(X[1],V[1]),(X[0],V[0]))

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

s.reset()

time.sleep(5)

k = 1 # k is the length of the run

while k < 8:
	L = [ Bool('x_%i%i' % (k,i)) for i in range(3) ]	
	#print L

	V.append(L[0])
	V.append(L[1])
	V.append(L[2])
		
	run_k = And(Run[k-1], substitute(alpha_T, (X[2],V[3*k-1]),(X[1],V[3*k-2]),(X[0],V[3*k-3]), (Y[2],V[3*k+2]),(Y[1],V[3*k+1]),(Y[0],V[3*k])))
	subp_k = substitute(P, (X[2],V[3*k+2]),(X[1],V[3*k+1]),(X[0],V[3*k]))

	Run.append(run_k)

	print run_k
	print subp_k

	s.add(run_k)
	s.add(Not(subp_k))

	result = s.check() # 

	if result == sat:
		print "The input FSM is unsafe -- for k = %i" %(k)
		sys.exit("exiting")
	else:
		print "All states at a distance %i are P-states -- safe for k = %i" %(k,k)
		print "Continuing for k = %i" %(k+1)

	s.reset()

	
	k = k + 1

	time.sleep(5)

