if __name__ == '__main__':
    # 1.
    # 编写Python程序判断字符串是否重复。（50
    # 分）
    # 2.
    # 编写Python程序打印输出字符串中重复的所有字符。（50
    # 分）
    # 3.  # 把下面的klist作为字典的键
    # # 并统计每个单词的词频
     klist = [ "good ", "good ", "study"," good ", "good", "study ","good ", " good", " study"," good ", "good",
               " study ", "good ", "good ", "study"," day ", "day", " up",
               " day ", "day", " up", " day ", "day", " up", " day ", "day",
               " up"," day ", "day", " up", " day ", "day", " up","day ", "day", " up"]
    # 临时存储数据源中的每个字符串，用于存储去空格后的数据
chars = ""
# 用于存放词
mlist = []
for k in klist:
    # 将每个元素存入此字符
    chars = k
    # 去除左右空格
    chars = chars.lstrip()
    chars = chars.rstrip()
    # 将mlist转为字符串查看是否存在过该列表出现过不添加
    if str(mlist).find(chars) == -1:
        mlist.append(chars)
    # 添加完毕后遍历词频输出出现次数
for k in mlist:
    print("出现词频词段", k, '\t\t', "出现次数：", str(klist).count(k))
    if __name__ == '__main__':

        klist = [
            "good ", "good ", "study",
            " good ", "good", "study ",
            "good ", " good", " study",
            " good ", "good", " study ",
            "good ", "good ", "study",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
        ]
        # 用set集合去重
        myset = set()
        for l in klist:
            myset.add(l.strip())
        print(myset)
        # 统计词频，存入dict字典
        mydict = {}
        for l in myset:
            # 计数
            num = 0
            for j in klist:
                if j.strip() == l:
                    num += 1
            mydict[l] = num
        # 查看结果
        print(mydict)