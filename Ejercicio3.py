num1=input("Ingrese un número: ");
num2=input("Ingrese un segundo número: ");
num3=input("Ingrese un tercer número: ");
suma=num1+num2+num3;
suma=int(suma)
if suma % 7 == 0:
    mensaje="Si es multiplo de 7";
    print(mensaje);
else:
    mensaje="No es multiplo de 7";
    print(mensaje);