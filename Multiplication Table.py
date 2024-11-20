n = int ( input ( "Enter a number : "))
a = 0
x = n*a
print (" Table of ", n )
for i in range (1,11,1):
    a=a+1
    for j in range (1,1+a):
        x=n*a
    print (n, " * " , a , " = " , x )
