n = int(input("Digite um número"))

fatorial = 1
for i in range(2, n + 1):
    fatorial *= i

print(f"{n}! = {fatorial}")
