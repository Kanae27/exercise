num = int(input("Enter a number: "))

if num % 4 == 0:
    print(f"{num} is a multiple of 4.")
elif num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

num_to_check = int(input("Enter a number to check: "))
divisor = int(input("Enter a number to divide by: "))

if num_to_check % divisor == 0:
    print(f"{num_to_check} divides evenly by {divisor}.")
else:
    print(f"{num_to_check} does not divide evenly by {divisor}.")
