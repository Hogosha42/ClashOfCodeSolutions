from functools import reduce

def unnest(x):
    return list(map(lambda l:sum(l, []),x))

matrix=[input().split()for i in range(9)]

rematrix = [unnest([[matrix[y][x:x+3]for y in range(i,i+3)]for x in range(0,9,3)])for i in range(0,9,3)]

for i in reduce(lambda x,y: x+y,rematrix):
    print(*i)