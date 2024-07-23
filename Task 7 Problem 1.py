#  Task 7 Problem 1

number=int(input("Enter number "))

def fibonacci (i):
    if i==0 :
        return 0
    elif i==1 :
        return 1
    else :
        return fibonacci (i-2) +fibonacci (i-1)
    
for x in range (number +1) :
    print (fibonacci(x))