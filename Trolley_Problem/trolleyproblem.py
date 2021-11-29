n = int(input()) 
o=[]
for i in range(n):
    # q: The number of people on the path
    # v: The individual value of each person on the path
    q, v = [int(j) for j in input().split()]
    o.append(q*v)
print(o.index(min(o))+1)
