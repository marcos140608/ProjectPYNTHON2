voltas=float(input("Quantos voltas?:"))
extensao=float(input("valor da extensão em metros?:"))
tempo=float(input("digite o valor do tempo?:"))
conextensao=extensao/1000
contempo=tempo/60
velocidademedia=voltas*conextensao/contempo
print(f"a velocidade media sera de {velocidademedia} km/h")




