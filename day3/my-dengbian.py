if __name__ == '__main__':
    num=int(input("请输入三角列数"))+1
    def triangles():
        n = [1]
        while True:
            yield n
            n = [x + y for x, y in zip([0] + n, n + [0])]
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == num:
            break