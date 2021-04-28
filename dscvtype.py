def dscvtype():
    s=input("Enter the Value ")
    if s in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' and len(s)==1:
        print("Charecter")
    elif s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(s)==1:
        print("Charecter")
    elif s in '123456789':
        print("Integer")
    elif s in '.':
        print("Float")
    elif s in '0':
        print(Zero)
    elif s in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' and len(s)>1:
        print("String")
    elif s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(s)>1:
        print("String")
    else:
        print("Wrong Choice")
