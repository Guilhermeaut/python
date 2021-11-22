n = int(input("Digite um valor positivo: "))

while (n < 0):
    print("Erro!!!! O valor digitado não é positivo. Digite novamente.")
    n = int(input("escreva um valor positivo: "))

if (n>=0):
    print("O valor é positivo!")