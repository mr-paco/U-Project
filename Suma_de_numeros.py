# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print ("Programaq ue suma cualquier cantidad de números que usted desse usar")
	print ("Ingrese un numero")
	a = int()
	a = int(raw_input())
	# b = int() # No es necesario inicializar b aquí
	# c = str() # No es necesario inicializar c aquí
	while True:# no hay 'repetir' en python
		print ("Ingrese otro Numero")
		b = int(raw_input()) # b se inicializa aquí
		a = a+b
		print ("El resultado es ="),a
		print ("Desea sumar otro numero Si o No? ")
		c = raw_input()
		if c=="no" or c=="No" or c=="NO": break
	print ("Muchas gracias")
