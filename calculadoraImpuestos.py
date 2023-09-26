#calculadora de impuestos.
#
#Debe aceptar un valor de punto flotante: el ingreso.
#A continuación, debe imprimir el impuesto calculado, redondeado a pesos
#totales. Hay una función llamada round() que hará el redondeo por ti
#- la encontrarás en el código de esqueleto del editor.

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 
