n=input()
print("true"if int(n)%sum(map(int,n))==0else"false")
