a=float(input("valor do produto??? "))
b=float(input("valor do produto??? "))
c=float(input("valor do produto??? "))
d=float(input("valor do produto??? "))
e=float(input("valor do produto??? "))
cash=float(input("dinheiro pago pelo cliente?: "))
troco= cash-(a+b+c+d+e)
print(f"o troco é: {troco:.2f}")