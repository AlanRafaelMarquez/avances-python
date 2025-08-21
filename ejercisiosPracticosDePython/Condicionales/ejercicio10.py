tipo_pizza = input("De que va ser tu pizza, vegetariana o de carnes: ")

if tipo_pizza.lower() == "vegetariana":
    print("Ingredientes vegetarianos:\nPimiento\nTofu\nMozzarella\nTomate\n")
elif tipo_pizza.lower() == "carnes":
    print("Ingredientes de carnes:\nPeperoni\nSalmón\nJamon\nMozzarella\nTomate\n")
else:
    print("Esa pizza no tenemos")
    
    
ingrediente_pizza = input("De que ingrediente quieres tu pizza: ")

if ingrediente_pizza == "peperoni"  :
    print(f"Tu pizza es de carnes y los ingredientes son:\n {ingrediente_pizza}\n Mozzarella\n Tomate\n ")
elif ingrediente_pizza == "salmon":
    print(f"Tu pizza es de carnes y los ingredientes son:\n {ingrediente_pizza}\n Mozzarella\n Tomate\n ")
elif ingrediente_pizza == "jamon":
    print(f"Tu pizza es de carnes y los ingredientes son:\n {ingrediente_pizza}\n Mozzarella\n Tomate\n ")
elif ingrediente_pizza == "pimiento":
     print(f"Tu pizza es vegetariana y los ingredientes son:\n {ingrediente_pizza}\n Mozzarella\n Tomate\n ")
elif ingrediente_pizza == "tofu":
     print(f"Tu pizza es vegetariana y los ingredientes son:\n {ingrediente_pizza}\n Mozzarella\n Tomate\n ")
else:
    print("Ese ingrediente no existe")
    
    

