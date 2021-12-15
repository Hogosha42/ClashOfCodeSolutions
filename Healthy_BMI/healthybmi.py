mass, height = [int(i) for i in input().split()]

bmi = mass/((height/100)**2)

def calcmassinc(x):
    return math.ceil(x*((height/100)**2))

if bmi<18.5:
    reccom= ["UNDERWEIGHT", calcmassinc(18.5-bmi)]
elif bmi<25:
    reccom= ["HEALTHY", 0]
elif bmi<30:
    reccom= ["OVERWEIGHT", calcmassinc(abs(25-bmi))]
else:
    reccom= ["OBESE", calcmassinc(abs(25-bmi))]

print(*reccom)
