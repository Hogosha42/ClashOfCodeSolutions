n, m, r, t = [int(i) for i in input().split()]
calc = (m-(r*t))-n >= 0
print("HAPPY"if calc else "NOT HAPPY")
