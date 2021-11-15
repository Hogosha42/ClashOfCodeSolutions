o=[0,1]
n=int(input())
for i in range(n-2):
 o.append(sum(o[-2:]))
print(*o if n>1 else[0])
