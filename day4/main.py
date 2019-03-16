import day4.quest1.p1 as l
if __name__ == '__main__':
    #l.sex()
    print("1:姓名性别")
    print("2:列表交集")
    print("3:用户注册明细")
    print("4:回文数")
    xz=input("请选择功能：")
    if int(xz)==1:
        l.sex()
    if int(xz) ==2:
        l.suiji()
    if int(xz) == 3:
        l.username()
    if int(xz) == 4:
        l.huiwen()

