def seclargest():
    l=list(map(int,input().split()))
    m1=max(l)
    l.remove(m1)
    print(max(l))