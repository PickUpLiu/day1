if __name__ == '__main__':
    num1=2
    num2=1
    sum=0
    for n in range(1, 21):
        sum+=num1/num2
        tem=num1
        num1=num1+num2
        num2=tem
    print(sum)
    if __name__ == '__main__':
        s = 0
        n = int(input("请输入一个整数："))
        num = 1
        for i in range(1, n + 1):
            num *= i
            s += num
        print("%d的阶乘累加和是%d" % (n, s))
        if __name__ == '__main__':
            d = {'x': 'A', 'y': 'B', 'z': 'C'}
            for k, v in d.items():
                print(k, '=', v)
            d = {'x': 'A', 'y': 'B', 'z': 'C'}
            L = [k + '=' + v for k, v in d.items()]
            print(L)
            ['y=B', 'x=A', 'z=C']
            if __name__ == '__main__':
                L = [x * x for x in range(1, 11) if x % 2 == 0]
                print(L)
                if __name__ == '__main__':
                    L = [x * x for x in range(1, 11)]
                    print(L)