if __name__ == '__main__':

    # 编写Python程序判断字符串是否重复。（50
    # 分）
    # 2.
    # 编写Python程序打印输出字符串中重复的所有字符。（50
    # 分）
    # 3.  # 把下面的klist作为字典的键
    # # 并统计每个单词的词频
    klist = ["good ", "good ", "study", " good ", "good", "study ", "good ", " good", " study", " good ", "good",
             " study ", "good ", "good ", "study", " day ", "day", " up",
             " day ", "day", " up", " day ", "day", " up", " day ", "day",
             " up", " day ", "day", " up", " day ", "day", " up", "day ", "day", " up"]
    myset=set()
    for l in klist:
        myset.add(l.strip())
    print(myset)
    mydisc={}
    for l in myset:
        num=0
        for j in klist:
            if j.strip()==l:
                num+=1
                mydisc[l]=num
    print(mydisc)