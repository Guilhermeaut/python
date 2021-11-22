n = int(input("Digite um numero para tabuada: "))

while(n <= 0):
    n = int(input("Erro! O numero digitado é negativo. Insira um valor positivo: "))

s = int(input("Digite ate qual numero da tabuada calcular: "))

for i in range(1, s+1, 1):
    r = n*i
    print(f"{n} X {i} = {r}")
    