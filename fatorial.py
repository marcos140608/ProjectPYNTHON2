valor = int(input("Digite o valor: "))

fat: int = 1
n: int = 1

while n <= valor:
    fat = fat * n
    n = n + 1

print(f"O valor do fatorial de {valor} será: {fat}")

