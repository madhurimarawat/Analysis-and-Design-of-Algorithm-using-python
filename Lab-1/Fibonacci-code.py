#To implement Fibonacci sequence
def Fibonacci(n):
    if n <=1:
        return n
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))
n1=int(input("Enter number of elements:"))
print("Fibonacci sequence:")
for i in range(n1):
    print(Fibonacci(i),end="  ")

