import  random
def sex(str=print()):
    name=input("请输入姓名:")
    sex= input("请输入性别:")
    str=[name,sex]
    nan=["男","boy","man","nan"]
    nv= ["女", "girl", "woman","nv"]
    if str[1] in nan:
        print(str[0],"先生你好")
    if str[1] in nv:
        print(str[0], "女士你好")
def suiji():
     mlist=[random.randint(1,100)for i in range(10)]
     nlist=[random.randint(1,100)for i in range(15)]
     print(mlist)
     print(nlist)
     myset = set(mlist)
     nyset=set(nlist)
     print("俩个列表的并集是：",myset|nyset)
     print("俩个列表的交集是：",myset&nyset)
     print("俩个列表的差集是：", myset-nyset)
def username():
     name=str(input("请输入用户姓名:"))
     if name.__len__()>=6:
         email=str(input("请输入邮箱："))
         if "@" in email:
             print("输入合法,填写无误")
         else:
             print("输入不合法")

     else:
         print("用户名不得少于六位")
def huiwen():
    ml=str(input("请输入一个字符串(1231321):"))
    if ml.__len__()%2!=0:
        print("输入合法")
        if ml==ml[::-1]:
            print("字符串为回文串")
        else:
            print("字符串不是回文串")
    else:
        print("请重新输入")


