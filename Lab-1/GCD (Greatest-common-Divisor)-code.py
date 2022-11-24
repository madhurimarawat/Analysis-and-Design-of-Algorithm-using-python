# To implement GCD (Greatest common Divisor) ( Euclidean algorithm ).
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
print ("The gcd of",a," and ",b,"is : ",end="")
print (computeGCD(a,b))
