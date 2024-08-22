print("Enter the numbers: ")
count=0
sumn=0
while (True):
    try:
        a= input()
        if (a=='done'):
                break
        else:
            a=int(a)
            count=count+1
            sumn=sumn+a
    except:
        print("Invalid Input!")
print("Count is: ",count)
print("Sum is: ",sumn)
print("Average is: ",sumn/count)
