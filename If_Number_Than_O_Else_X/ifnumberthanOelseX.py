nlist=[]
for i in range(5):
    nlist.append(input().split())
values=nlist[-1]
nlist=nlist[:-1:]

def check(x):
    for i,w in enumerate(x):
        if w==values[i]:
            x[i]="O"
        else:
            x[i]="X"
    return x


for i in list(map(check,nlist)):
    print(*i)
