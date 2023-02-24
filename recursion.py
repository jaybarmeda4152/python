def func_recursive(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0 
    else:
        return n * func_recursive(n-1)


for i in range(6):
    # inp = int(input("Enter the number to find out factorial number: "))
    print("The factorial of given number is ",func_recursive(i))