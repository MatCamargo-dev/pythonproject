from aula7televisao import Televisao
from aula7calculadora1 import Calculadora
from aula8contadorletras import contador_letras,teste

if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ["cachorro", "gato", "elefante"]
    total_letras = contador_letras(lista)
    print("total de letras por palavra de lista : {}".format(total_letras))
    print(teste())