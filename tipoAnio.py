#calendario Gregoriano (en 1582), se utiliza la siguiente regla para
#determinar el tipo de año:
#
#si el número del año no es divisible entre cuatro, es un año común.
#de lo contrario, si el número del año no es divisible entre 100, es un
#año bisiesto.
#de lo contrario, si el número del año no es divisible entre 400, es un
#año común.
#de lo contrario, es un año bisiesto.

# -- ROSA HERRERA -- ESIT -- SEPTIEMBRE / 2023

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
	
