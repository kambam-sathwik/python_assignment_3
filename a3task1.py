
num=int(input("Enter a number: "))

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

print(f"factorial of {num} is {factorial(num)}")