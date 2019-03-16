if __name__ == '__main__':
    m=[1,2,3,4,5,6,7,8,9]
    my = input("请输入您想求得数字")
    for i in m:
        if i==int(my)+1:
            break
        for j in m:
            if i==j:
              print(i,"*",j,"=",i*j,sep="")
              break
            else:
                print(i, "*", j, "=", i * j, sep="",end=" ")