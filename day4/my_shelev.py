import  shelve
shv=shelve.open(r"shv.db")
try:
    one=shv["gg"]
    print("one=",one)
except Exception as e:
    print("exception")
finally:
    print("finally")
    shv.close()