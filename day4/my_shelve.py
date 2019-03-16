import  shelve
shv=shelve.open(r"shv.db")
one=shv["one"]
print("one=",one)
shv.close()