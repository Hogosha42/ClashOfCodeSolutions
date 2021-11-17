q = input()

qwerty="1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./ "
dvorak="1234567890[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz "
o=[]
for i in q:
    o.append(dvorak[qwerty.index(i)])
print(''.join(o))
