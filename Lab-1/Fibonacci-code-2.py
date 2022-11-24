#To implement Fibonacci sequence
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
n1=int(input("Enter number of elements:"))
for i in range(n1):
   print(Fibonacci(i),end="  ")
