I=input
I()
s=I().split()
l,r,f,b=[s.count(x)for x in"LRFB"]
I(int(((l-r)**2+(f-b)**2)**0.5))
