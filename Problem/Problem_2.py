a=[] #List
M=str(input()) #user input string
a.append(M) #appending the value in the list
N=str(input()) #user input string 
for i in range(0,len(a)): #condition for loop
    if N==a[i]:# condition
        print("The index value of",N,"in the list is:",i)
        break # braking the loop
else:
    print("Better Luck Next Time") #else condition
