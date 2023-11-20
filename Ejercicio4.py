num1=int(input("Ingrese un número: "));
num2=int(input("Ingrese un segundo número: "));
num3=int(input("Ingrese un tercer número: "));
suma=num1+num2+num3;
promedio=suma//3;
promedio=str(promedio)
print("Promedio: " + promedio)
if suma % 2 == 0:
    mensaje="El promedio es par";
    print(mensaje);
else:
    mensaje="El promedio es impar";
    print(mensaje);
