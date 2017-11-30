#!
import datebase.english as en
import datebase.math as mt
import random
tj=[0,0,0,0,0,0,0,0,0]
last_one = None
while(1):
    content = en.words_in_u4
    len_1 = len(content)-1
    t = random.randint(0,len_1)
    content_in = input(content[t][0])
    print(content[t][1])
    if content_in =='y':
        if last_one != None:
            print("删除：%s\t%s"%(content[last_one][0],content[last_one][1]))
            content.pop(last_one)
            if last_one < t:
                t = t - 1
        else:print("这是第一次，别想着删上次的\n")
    elif content_in == 't':
        for i in content:
            print(i[0],"  \t",i[1])
        print("共计%d个内容"%len(content))
    last_one = t
