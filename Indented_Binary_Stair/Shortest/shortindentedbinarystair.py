n=int(input())
for i in range(n+1):
 o=bin(i)[2:]
 print(str(o).rjust(len(bin(n)),' '))
