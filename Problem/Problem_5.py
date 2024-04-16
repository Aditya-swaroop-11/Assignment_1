a = [] #making a list
b = int(input() #user input term
for i in range(b): #loop for b numbers
    c = int(input()) #user input nubers
    a.append(c) #appending to the list
for i in range(len(a)): #loop for sorting
    M=i # taking a minimum value of i
    for j in range(i + 1, len(a)): #for comparision
        if a[j]<a[M]: #compreing the values in the list
            M= j
    a[i], a[M] = a[M], a[i] #comparision between i and m
print(a)# printing the shorted value