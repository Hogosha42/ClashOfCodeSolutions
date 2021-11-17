import re
n=input()
r=re.findall('..',n)
r=list(map(lambda x:x[::-1],r))
print(''.join(r))if len(n)%2==0 else print(''.join(r)+n[-1])
