num = int(input("Enter a number: "))
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print(f"Divisors of {num}: {divisors}")
