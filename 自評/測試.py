with open("w7.txt", "r", encoding="utf-8") as txt:
    TT = txt.readlines()
    T = TT[1:]
    #print(T)
    k = []
    for i in range(len(T)):
        tl = T[i].strip()
        #print(tl)
        g = tl.split( )
        #print(g)
        for j in range(len(g)):
            if g[j] != "" :
                k.append(g[j])
absent = [i for i in k if k.count(i) == 1]
print(absent)