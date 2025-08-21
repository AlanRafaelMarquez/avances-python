precio = input("Dime el precio de un producto con centimos: ")

print(precio[:precio.find(".")],"euros y ",precio[precio.find(".")+1:],"centimos")