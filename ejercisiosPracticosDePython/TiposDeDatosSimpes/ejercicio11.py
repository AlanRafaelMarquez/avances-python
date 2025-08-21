dinero_depositado = int(input("Dime la catidad de dinero que quieres depositar: "))

interes_primer =  dinero_depositado * 0.04 
interes_segundo = interes_primer * 2 
interes_tercero = interes_primer * 3 

resultado_sum = interes_primer + dinero_depositado
resultado_sum2 = interes_segundo + dinero_depositado
resultado_sum3 = interes_tercero+ dinero_depositado

print(f"El interes del primer año es : {resultado_sum}, el segundo año es {resultado_sum2}, el tercer año es {resultado_sum3}")