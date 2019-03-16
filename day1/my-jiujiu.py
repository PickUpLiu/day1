if __name__ == '__main__':
    i=1
    while i<10:
        b=1
        while b<=i:
            print(b,"*",i,"=",b*i,"\t",end='')
            b+=1
        i+=1
        print()
    print("结束")
    if __name__ == '__main__':
        m9=[1,2,3,4,5,6,7,8,9]
        for i in m9:
            for j in m9:
             print(str(i)+"*"+str(j)+"="+(str(i*j).ljust(3)),end="")
             if i==j:
                 print()
                 break
