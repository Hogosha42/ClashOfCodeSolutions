o=[tuple(input().split())for i in range(int(input()))]
o.sort(key=lambda x:int(x[0]))
print(*[x[1]for x in o])
