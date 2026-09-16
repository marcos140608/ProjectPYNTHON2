n: int = 1
maior: float = 0
menor: float = 0

while n <= 100:
    valor = float(input(f"Digite o {n}º número positivo: "))

    if valor > 0:
        if n == 1:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor

            if valor < menor:
                menor = valor

        n += 1
    else:
        print("Digite somente valores positivos.")

print(f"O maior é {maior} e o menor é {menor}")

















