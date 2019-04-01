l = input().split()
i = 0
while (i < len(l) ):
    j = 0
    status = True
    while (j < len(l)):
        if (i != j and l[i] == l[j]):
            status = False    
        j += 1
    if (status == True):
        print(l[i], end = " ")
    i += 1