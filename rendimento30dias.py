valor=float(input("Digite o valor investido: "))
tipo=int(input("selecione o tipo de investimento:"))

if tipo==1:
    rendimento=valor + (valor*0.03)
    print(f"o valor que vai ter depois de 30 dias sera de R$ {rendimento:.2f}")
elif tipo==2:
    rendimento=valor + (valor*0.05)
    print(f"o valor que vai ter depois de 30 dias sera de R$ {rendimento:.2f}")

