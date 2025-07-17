

with open("prueba.txt", "w") as texto:
    texto.write("primero linea\nsegunda linea\ntercera linea")



with open("prueba.txt", "r") as texto:
    lista = texto.readlines()
    print(lista)