#Write a recursive function to return the nth Fibonacci number.
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter the number: "))
if n<0:
    print("The number is not valid")
else:
    print(f"The Fabonacci Series of given number {n} is : ",fibonacci(n))