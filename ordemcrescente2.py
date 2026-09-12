A = float(input("Digite o primeiro valor: "))
B = float(input("Digite um valor maior que o primeiro: "))
C = float(input("Digite um valor maior que o segundo: "))
D = float(input("Digite o quarto valor: "))

if not (A < B < C):
    print("Os três primeiros valores devem estar em ordem crescente.")
else:
    if D <= A:
        print(D, A, B, C)
    elif D <= B:
        print(A, D, B, C)
    elif D <= C:
        print(A, B, D, C)
    else:
        print(A, B, C, D)
