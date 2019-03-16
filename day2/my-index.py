import random
if __name__ == '__main__':
    mstr="good good study,day day up"
    ms=mstr.index("good")
    print(ms)
    msr = "good good study,day day up"
    mrs=msr.index("good",1)
    print(mrs)
    m = "good good study,day day up"
    mc=m.index("good",1,10)
    print(mc)
    mlist=list()
    mlist.append("yi")
    print(mlist)
    mlist.insert(1,"er")
    print(mlist)
    val=mlist.pop()
    print("mlist.pop={popval}".format(popval=val))
    myname=[3,7,4,2]
    print(myname)
    random.shuffle(myname)
    print(myname)
    #永久
    myname.sort(reverse=True)
    print(myname)
    nyname=sorted(myname,reverse=True)
    print(nyname)
    m=[1,"a",5,'c',6]
    mlen=len(m)
    print(mlen)
    mm=[1,2,3,5]
    for i in mm:
        print("mm[{0}]={1}".format(i.__index__(),i))
    mi=[1,2,3,4]
    print("mi[{0}]={1}".format(mi[2].__index__(),mi[2]))
    li=[1,2,3,4]
    print(id(li))
    p=[1,2,3,4,5,6,7,8]
    t=2;
    print(t in p)
    print(t not in p)
    mo=[random.randint(0,100) for i in range(0,10)]
    print(mo)
    mp=[1,2,3,5,4,5,2,2,2,3,4]
    print(mp.count(2))

