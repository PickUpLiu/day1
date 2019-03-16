if __name__ == '__main__':
    try:
        print(5/0)
    except ZeroDivisionError as e:
      print("ZeroDivisionError")
      print(e)
      print("good")