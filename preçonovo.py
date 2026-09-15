precoatual=float(input("digite o preço atual:"))
mediamensal=float(input("digite o valor da media mensal:"))

if mediamensal<500 and precoatual<30:
    porcentagem=10/100
    preconovo = precoatual + (precoatual * porcentagem)
    print(f"{preconovo:.2f} reais será o preço novo")
elif 500 <= mediamensal < 1000 and 30 <= precoatual <80:
    porcentagem=15/100
    preconovo = precoatual + (precoatual * porcentagem)
    print(f"{preconovo:.2f} reais será o preço novo")
elif mediamensal >= 1000 and precoatual >= 80:
    porcentagem=5/100
    preconovo = precoatual - (precoatual * porcentagem)
    print(f"{preconovo:.2f} reais será o preço novo")
else:
    preconovo = precoatual
    print(f"{preconovo:.2f} reais será o preço novo")


