num1=input("Ingrese un número: ");
num2=input("Ingrese un segundo número: ");
num3=input("Ingrese un tercer número: ");
if num1>num2:
    mensaje="El primer número es el mayor";
    print(mensaje);
elif num2>num1 and num2>num3:
    mensaje="El segundo número es el mayor";
    print(mensaje);
elif num3>num2 and num3>num1:
    mensaje="El tercer número es el mayor"
    print(mensaje);
