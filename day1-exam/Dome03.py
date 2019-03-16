import random
if __name__ == '__main__':
      num=int(input("请您输入一个数字"))
      s=random.choice(range(num*2))
      if num>s:
            print("you win")
      else:
            print("you lose")
      print(s)
