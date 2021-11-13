s_1 = list(map(int, input().split(' ')))
s_2 = list(map(int, input().split(' ')))

if len(s_1)==len(s_2):
    print(*list(map(lambda x,y: x+y, s_1, s_2))
else:
    print("Invalid")
