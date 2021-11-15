n = int(input())
e= list(map(int, input().split())) #split the string into a list of integers
for i in e:
    if e.count(i)==1:  
        print(i)        #print the only singular element in the list
        
