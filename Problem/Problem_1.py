a=[] #making a list to store 
M=int(input()) #user input of M number which is less then 10^6 and greater then 1
b=input()  #user input of number in the format 1;2;3;4;5
a.append(b) #appending the value of b(user input) in the list a[]
sum=0
c=""
if(1<=M<=10**6):#condition for M
    for i in b: #range of i
        if (i==";"): #condition for cheaking for ;
            sum=sum+int(c) 
            c=""
        else: #else condition 
            c=c+i
sum=sum+int(c)    #summation of integer number of the list a[]         
print(sum) #printing the total sum value