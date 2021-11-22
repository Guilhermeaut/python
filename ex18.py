a=float(input("qual sua altura??? "))
b=float(input("qual sua peso??? "))
sexo = input("Digite o sexo (F/M): ")

sexo = input("Digite o sexo (F/M): ")

imc = b / (a * a)

if sexo == 'F':
    if imc < 19:
        print("Abaixo do peso!")
    elif imc < 24:
        print("Peso ideal!")
    else:
        print("Acima do peso!")

if sexo == 'M':
    if imc < 20:
        print("Abaixo do peso!")
    elif imc < 25:
        print("Peso ideal!")
    else:
        print("Acima do peso!")