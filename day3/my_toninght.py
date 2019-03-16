
# 等边三角形
# 九九乘法表
def multiplicationTable(num=9):
    i = 1
    while i <= num:
        j = 1
        while j <= i:
            print(j, "X", i, "=", str(j * i).rjust(2), end="")
            j += 1
        i += 1
        print()
# 菱形
def rhombus(num=10):
    num = num // 2
    i = 1
    while i <= num:
        j = num
        while i < j:
            print(" ", end="")
            j -= 1
        j = 1
        while j <= i * 2 - 1:
            print("*", end="")
            j += 1
        i += 1
        print()
    i = 1
    while i <= num - 1:
        j = 1
        while j <= i:
            print(" ", end="")
            j += 1
        j = 1
        while j <= (num - i) * 2 - 1:
            print("*", end="")
            j += 1
        i += 1
        print()
# 1到n左对齐
def lefJustifying(num=100):
    for l in range(1, num + 1):
        print(str(l).rjust(str(num + 1).__len__() + 1), end="")
        if l % 10 == 0:
            print()
def sanJiao(num=6):
    for i in range(1, num):
        for j in range(1, num - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print("* ", end="")
        print("")
def shuLie(len=10):
    mlist=[i for i in range(0,len*10)]
    for i in mlist:
        if(i%10==9 and i!=0):
            print(str(i).ljust(5))
        else:
            print(str(i).ljust(5),end="")