import pickle
if __name__ == '__main__':
    with open(r"F:\a.txt",mode="wb") as f:
        pass
    name="simple"
    pickle.dump(name,f)
with open(r"F:\a.txt", mode="wb") as f:
  pass
  name=pickle.load(f)
  print("name=",name)
