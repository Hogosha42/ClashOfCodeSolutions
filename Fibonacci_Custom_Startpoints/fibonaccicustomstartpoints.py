I=input
t=int(I())
o=[int(I()),int(I())]
print(o[0])
for i in range(t-1):print(o[-1]);o.append(sum(o[-2:]))
