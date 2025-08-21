puntuacion = float(input("Dime la puntuacion del usuario de 0.0, 0.4 y 0.6 : "))
dinero = 2400

if puntuacion == 0.0:
    print(f"Tus ingresos son 0 ")
    print("Tu nivel es Inacepltable")
elif puntuacion >= 0.1 and puntuacion <= 0.3:
    print("No existe ese nivel lol ")
elif puntuacion == 0.4:
    print(f"Tus ingresos son: {dinero * 0.4} ")
    print("Tu nivel es Acepltable")
elif puntuacion == 0.5:
    print("No existe ese nivel")
elif puntuacion == 0.6:
    print(f"Tus ingresos son: {dinero * 0.6} ")
    print("Tu nivel es Mentor")
else:
    print("No existe ese nivel")  
    
    
    
    
    
    
    
    
    