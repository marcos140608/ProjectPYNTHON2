valor1 = int(input("Digite o valor: "))
valor2 = int(input("Digite o valor 2: "))

maior: int
menor: int
soma: int = 0
n: int

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

n = menor

while n <= maior:
    if n % 2 != 0:
        soma = soma + n

    n = n + 1

print(f"A soma de todos os números ímpares entre o maior e menor será: {soma}")











