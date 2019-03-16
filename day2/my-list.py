if __name__ == '__main__':
    mlist=list()
    ms=[]
    print(type(mlist))
    print(type(ms))
    mlist.append("一")
    mlist.append("三")
    #给定位置添加
    mlist.insert(0, "二")
    print(mlist)
    ms.insert(0,"二")
    print(ms)
    mlist.pop(0)
    print(mlist)
    del mlist[0]
    print(mlist)
    mlist.remove("三")
    print(mlist)
    mlist.append("yi")
    print(mlist)
    mlist.clear()
    print(mlist)
    str=[1,2,3,4,5]
    str.reverse()
    print(str)