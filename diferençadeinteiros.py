valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    resultado = valor1 - valor2
else:
    resultado = valor2 - valor1

print(f"A diferença entre os valores é {resultado}")