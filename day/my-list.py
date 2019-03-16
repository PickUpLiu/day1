if __name__ == '__main__':
    mlist=[1,2,3]
    nlist=["a","b","c"]
    qlist=[str(m)+n for m in mlist for n in nlist \
           if m%2==0]
    print(qlist)