if __name__ == '__main__':
    str1=int(input("请输入第一个人的出生年月:(20180501)"))
    str2=int(input("请输入第二个人的出生年月:(20180501)"))
    print(str1)
    print(str2)
    if str1>str2:
        print("str2的年龄大")
    if str1<str2:
        print("str1的年龄大")
    else:
        print("年龄相同")