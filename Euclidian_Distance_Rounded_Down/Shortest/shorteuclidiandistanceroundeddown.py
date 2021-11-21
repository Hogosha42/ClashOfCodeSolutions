I=int
p,o=[I(i)for i in input().split()]
e,l=[I(i)for i in input().split()]
print(I((((p-e)**2+(o-l)**2)**.5)//1))
