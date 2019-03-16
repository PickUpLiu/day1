if __name__ == '__main__':
    mscore=0
    mscore=input("enter your score:")
    mscore=int(mscore)
    print(mscore)
    if mscore<=100 and mscore>=0:
        if mscore<60:
            print("bad")
        if mscore<=80 and mscore>=60:
            print("good")
        if mscore<=100 and mscore>80:
            print("excsllent")


