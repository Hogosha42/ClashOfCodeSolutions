for i in list(map(lambda x:[x[:len(x)//2].count("o"),x[len(x)//2:].count("o")],[input()[3:-3]for i in range(int(input()))])):print(*i)
