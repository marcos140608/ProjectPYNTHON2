A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))
C = float(input("Digite o coeficiente C: "))

if A == 0:
    print("Não é uma equação do segundo grau.")
else:
    delta = B**2 - 4*A*C

    if delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        x1 = -B / (2*A)
        print(f"Existe apenas uma raiz real: {x1}")

    else:
        x1 = (-B + delta**0.5) / (2*A)
        x2 = (-B - delta**0.5) / (2*A)
        print(f"Existem duas raízes reais: {x1} e {x2}")