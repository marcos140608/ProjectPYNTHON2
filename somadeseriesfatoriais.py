N = int(input("Digite o valor: "))
fat: int = 1
soma: float = 1.0
n: int = 1

while n <= N:
    fat = fat * n
    soma = soma + 1 / fat
    n = n + 1

print(f"A soma da série será: {soma}")













