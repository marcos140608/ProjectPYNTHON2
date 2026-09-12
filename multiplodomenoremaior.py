A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

if menor == 0:
    if maior == 0:
        print("0 é múltiplo de 0.")
    else:
        print(f"{maior} não é múltiplo de 0.")
elif maior % menor == 0:
    print(f"{maior} é múltiplo de {menor}.")
else:
    print(f"{maior} não é múltiplo de {menor}.")



