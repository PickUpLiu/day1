if __name__ == '__main__':
     name=input("your name:")
     print("good to you {0}".format(name))
if __name__ == '__main__':
        score=0
        score=int(input("请输入一个分数:"))
        if score<=100 and score>0:
            print("输入合法")
            if score<60:
                print("垃圾")
            if score>60 and score<=80:
                print("良好")
            if score>=80 and score<=100:
                print("牛逼")
if __name__ == '__main__':
    mlist=[0,1,2,3,4,5]
    for i in mlist:
        print(i)
if __name__ == '__main__':
    mlist=["good","good","study"]
    nlist=["day","day","up"]
    for i in mlist+nlist:
        print(i,sep="*",end="")
if __name__ == '__main__':
    for i in range(5):
        print("中国牛逼",sep="-",end="")