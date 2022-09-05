import numeros


def preguntar():

    print("Bienvenido a Farmacia Python")


    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres retirar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa opción es incorrecta")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()      
