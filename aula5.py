lista = [1, 3, 5, 7]
lista_animal = ["cachorro", "gato", "elefante"]
#print(lista_animal[1])

lista.sort() #Para ordenar a lista
lista.reverse() #Para inverter a ordem dos caracteres
insert #Para adicionar a um lugar especifico
print(len(lista_animal)) #Para identificar quantos elementos tem na lista
if "lobo" in lista_animal:
    print("existe um lobo na lista")
else:
    print("nao existe um lobo na lista. Sera incluido")
    lista_animal.append("lobo") #Para adicionar 
    print(lista_animal)

lista_animal.pop(0) #Para retirar
print(lista_animal)

lista_animal.remove("elefante") #Para retirar 
print(lista_animal)