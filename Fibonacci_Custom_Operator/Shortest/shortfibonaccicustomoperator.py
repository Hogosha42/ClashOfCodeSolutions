a,b,o,k=open(0)
l=[a,b]
if o[:1]in"+-*/":
 for i in range(int(k)):l.append(eval(f"int({l[-2]}{o}{l[-1]})"))
 print(l[-1])
else:print("ERROR")
