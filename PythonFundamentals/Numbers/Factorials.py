def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # same as result = result * i
    return result


# Get input from the user
num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
