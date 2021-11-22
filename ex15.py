a=float(input("qual sua altura??? "))
b=float(input("qual sua peso??? "))
imc=b/(a*2)
 
if imc < 20:
    print("Abaixo do peso!")
elif imc < 25:
    print("Peso ideal!")
else:
    print("Acima do peso!")