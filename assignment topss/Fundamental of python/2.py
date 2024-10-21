num = int(input("Enter the number : "))

factorial = int(input("Enter the factorial variable : "))

for i in range(1,num+1):
    factorial *=i

print(f"the factorial of {num} is {factorial}")