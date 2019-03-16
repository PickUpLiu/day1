if __name__ == '__main__':
        mfile=open(r"C:\Users\Dell\PycharmProjects\untitled\day4\c.doc","rb")
        mbool=mfile.read()
        print(mbool)

        nfile=open(r"C:\Users\Dell\PycharmProjects\untitled\day4\d.doc","wb")
        nn=nfile.write(mbool)
        print(nn)