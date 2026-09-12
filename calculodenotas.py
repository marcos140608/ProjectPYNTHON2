A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
C = float(input("Digite a terceira nota: "))
D = float(input("Digite a quarta nota: "))

media = (A + B + C + D) / 4

if media >= 6:
    print("Aprovado")
elif media >= 3:
    print("Exame")
else:
    print("Reprovado")

