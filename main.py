from func import f,ff, retornaPI, MiClase
from constantes import *

def main():
    print(retornaPI())
    valor = input("ingrese f o ff: ")
    if valor == "f":
        f()
    elif valor == "ff":
        ff("Dario")
    else:
        print("Opción no válida")
        
    print("************************************************")
    mi_clase = MiClase("Argumento 1")
    print(mi_clase.argumento1)
    print(CONSTANTE)
    print(OTRA)

if __name__ == '__main__':
    main()