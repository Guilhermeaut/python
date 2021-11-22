A=input("digite o lado a do seu triangulo")
B=input("digite o lado b do seu triangulo")
C=input("digite o lado c do seu triangulo")

(A<(B+C) and B<(A+C) and C<(A+B))
if (A==B and B==C):
    print("triangulo equilatero")
elif(A==B and A==C and C==B):
    print("trangulo isosceles")
else:
    print("triangulo escaleno")