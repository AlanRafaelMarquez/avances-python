tabla = int(input("Dime la tabla de multiplicar que te muestres: "))

for i in range(1,10+1):
    mult = tabla*i
    print(f"{i} X {tabla} = {mult}")
    
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")