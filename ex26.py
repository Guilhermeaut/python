n = int(input("Digite um numero para tabuada: "))

while(n <= 0):
    n = int(input("Erro! O numero digitado é negativo. Insira um valor positivo: "))
 
for i in range(1, 11, 1):
    r = n*i
    print(f"{n} X {i} = {r}")