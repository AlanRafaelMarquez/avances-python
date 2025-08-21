palabra1=input("\nIngresa palabra 1:")
palabra2=input("Ingresa palabra 2:")

if sorted(palabra1) == sorted(palabra2):
    print(f"\n{palabra1} y {palabra2} Son Anagramas")
    
else:
    print(f"\n{palabra1} y {palabra2} No son Anagramas")