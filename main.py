#!
import datebase.math as mt
import random
tj=[0,0,0,0,0,0,0,0,0]
while(1):
    t1 = random.randint(0,8)
    t2 = random.randint(0,8)
    t3 = random.random()
    tj[int(t2)]=tj[int(t2)]+1
    # print(t)
    input(mt.integar_ret_formula11[int(t2)][0])
    print("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t"%(tj[0],tj[1],tj[2],tj[3],tj[4],tj[5],tj[6],tj[7],tj[8]),mt.integar_ret_formula11[int(t2)][1])
    # print("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(tj[0],tj[1],tj[2],tj[3],tj[4],tj[5],tj[6],tj[7],tj[8]))
