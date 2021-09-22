import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2)-(4 * a * c)

if a == 0:
    print("O valor de a, deve ser diferente de zero!")

elif delta < 0:
    print("Sem raízes reais")

else:
    x1 = (-b - delta ** 0.5)/(2 * a)
    x2 = (-b + delta ** 0.5)/(2 * a)

print("As raizes da equação são: " "x1 =",x1, "e x2 =", x2)