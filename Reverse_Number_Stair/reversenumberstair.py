n=int(input())
o=""
for i in range(1,n+1):
    o+=str(i)
for i in range(n):
 print(str(o).rjust(n,'+'))
 o=o[:-1]
