from z3 import *

"""Encoding: i_j_k is True if jth column has k as Attribute Value in Attribute row i.
Eg. Color_2_Yellow means 2nd column has Yellow color in Color row attribute"""


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


Hash = {"Color": ["Red", "Green", "Ivory", "Yellow", "Blue"],
        "Nationality": ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
        "Drink": ["Coffee", "Milk", "OrangeJuice", "Tea", "Water"],
        "Animals": ["Dogs", "Snails", "Fox", "Horse", "Zebra"],
        "Smoke": ["Kools", "OldGold", "Chesterfields", "LuckyStrike", "Parliaments"]}
Number = ['1', '2', '3', '4', '5']
# print(Hash)

solve_stack = Solver()
for i in Hash.keys():
    for j in Number:
        tmp = []
        for k in Hash[i]:
            tmp.append(Bool(i + '_' + j + '_' + k))
        # print(tmp)
        solve_stack.add(exactly_one(tmp))
    for k in Hash[i]:
        tmp = []
        for j in Number:
            tmp.append(Bool(i + '_' + j + '_' + k))
        # print(tmp)
        solve_stack.add(exactly_one(tmp))

cond = []
for i in range(15):
    cond.append([])
cond[8].append(Bool('Drink_3_Milk'))
cond[9].append(Bool('Nationality_1_Norwegian'))
cond[14].append(Bool('Color_2_Blue'))
for j in range(1, 15):
    if j != 8 and j != 9 and j != 14:
        for i in range(1, 6):
            if j == 1:
                if i != 1 and i != 2:
                    tmp1 = Bool('Color_'+str(i)+'_Red')
                    tmp2 = Bool('Nationality_'+str(i)+'_Englishman')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 2:
                if i != 1:
                    tmp1 = Bool('Nationality_'+str(i)+'_Spaniard')
                    tmp2 = Bool('Animals_'+str(i)+'_Dogs')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 3:
                if i != 2 and i != 3:
                    tmp1 = Bool('Color_'+str(i)+'_Green')
                    tmp2 = Bool('Drink_'+str(i)+'_Coffee')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 4:
                if i != 1 and i != 3:
                    tmp1 = Bool('Nationality_'+str(i)+'_Ukrainian')
                    tmp2 = Bool('Drink_'+str(i)+'_Tea')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 5:
                if i <= 4 and i != 2:
                    tmp1 = Bool('Color_'+str(i)+'_Ivory')
                    tmp2 = Bool('Color_'+str(i+1)+'_Green')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 6:
                tmp1 = Bool('Smoke_'+str(i)+'_OldGold')
                tmp2 = Bool('Animals_'+str(i)+'_Snails')
                cond[j].append(And(tmp1, tmp2))
            elif j == 7:
                if i != 2:
                    tmp1 = Bool('Smoke_'+str(i)+'_Kools')
                    tmp2 = Bool('Color_'+str(i)+'_Yellow')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 10:
                if i <= 4:
                    tmp1 = Bool('Animals_'+str(i)+'_Fox')
                    tmp2 = Bool('Smoke_'+str(i+1)+'_Chesterfields')
                    cond[j].append(And(tmp1, tmp2))
                    tmp1 = Bool('Animals_'+str(i + 1)+'_Fox')
                    tmp2 = Bool('Smoke_'+str(i)+'_Chesterfields')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 11:
                if i <= 4:
                    tmp1 = Bool('Animals_'+str(i)+'_Horse')
                    tmp2 = Bool('Smoke_'+str(i+1)+'_Kools')
                    cond[j].append(And(tmp1, tmp2))
                    tmp1 = Bool('Animals_'+str(i + 1)+'_Horse')
                    tmp2 = Bool('Smoke_'+str(i)+'_Kools')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 12:
                if i != 3:
                    tmp1 = Bool('Smoke_'+str(i)+'_LuckyStrike')
                    tmp2 = Bool('Drink_'+str(i)+'_OrangeJuice')
                    cond[j].append(And(tmp1, tmp2))
            elif j == 13:
                if i != 1:
                    tmp1 = Bool('Nationality_'+str(i)+'_Japanese')
                    tmp2 = Bool('Smoke_'+str(i)+'_Parliaments')
                    cond[j].append(And(tmp1, tmp2))

for i in range(1, 15):
    # print(cond[i])
    solve_stack.add(exactly_one(cond[i]))
# print(solve_stack)
solve_stack.check()
model = solve_stack.model()
print('[', end=' ')
for d in model.decls():
    if model[d] == True:
        print(d.name(), ':', model[d], ' ', end=' ')
print(']')
print()
for d in model.decls():
    if model[d] == True:
        tmp_str = d.name().split('_')
        if tmp_str[2] == 'Water':
            print('* ' + tmp_str[2] + ' by House ' + tmp_str[1])
        if tmp_str[2] == 'Zebra':
            print('* ' + tmp_str[2] + ' by House ' + tmp_str[1])
