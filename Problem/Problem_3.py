a = [] #list
M = input() #string input from user
b = M.split() # using spilit function
for i in range(len(b)-1,-1,-1): #condition
    a.append(b[i]) #appending the value
for ele in a:  #condition for element
    print(ele) #printing the reverse value
