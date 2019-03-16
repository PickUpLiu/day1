if __name__ == '__main__':
    str=input("请输入一个字符串：")
    strr=""
    for i in str:
        if(str.count(i)>1):
            if(strr.find(i)==-1):
                print("重复的字段为：",i,"重复的次数:",str.count(i))
                strr+=i
    print("重复字段的集合为：",strr)
    if __name__ == '__main__':
        str = input("请任意输入一段字符串")
        print(str.__len__())
        myset = set(str)
        if myset.__len__() == str.__len__():
            print("无重复")
        else:
            print("有重复的字符")
            for i in myset:
                if str.count(i) >= 2:
                    print(i, "出现了", str.count(i), "次")