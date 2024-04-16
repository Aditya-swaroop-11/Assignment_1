a = [] #list 
M = int(input()) # taking input from the user
for i in range(0, M):# condition for loop
    b = int(input()) #user input numbers
    a.append(b) # appending the values to the list
for i in range(0, len(a)): #cheaking for the condition
    if a[i] >= 50: #condition
        print(a[i])
for i in range(0, len(a)):
    if 30 <= a[i] <= 40:#condition
        print(a[i])
for i in range(0, len(a)):
    if 10 <= a[i] <= 20:#condition
        print(a[i]) #printing the outcome