def match(w):
    c=0
    l=[]
    for x in w:
        if x[0]==x[-1] and len(x)>1:
            c=c+1
            l.append(x)

    print("Word matching are",l)
    return c

count=match(["343","madam","567"])
print("count:",count)