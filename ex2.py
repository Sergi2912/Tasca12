def crear_fitxer():
    with open("tasques.txt", "w") as f:
        print("Fitxer tasques.txt creat \n")

def inserir_element(a):
    with open("tasques.txt", "a") as f:
        f.write(a + "\n")
        print(f"Tasca '{a}' afegida al fitxer.\n")

def modificar_element(antiga, nova):
    with open("tasques.txt", "r") as f:
        tasques = f.readlines()
    with open("tasques.txt", "w") as f:
        for tasca in tasques:
            if tasca.strip() == antiga:
                f.write(nova + "\n")
                print(f"Tasca '{antiga}' modificada a '{nova}'.\n")
            else:
                f.write(tasca)

def eliminar_element(a):
    with open("tasques.txt", "r") as f:
        tasques = f.readlines()
    with open("tasques.txt", "w") as f:
        for tasca in tasques:
            if tasca.strip() != a:
                f.write(tasca)
            else:
                print(f"Tasca '{a}' eliminada del fitxer.\n")

def llistar_fitxer():
    with open("tasques.txt", "r") as f:
        tasques = f.readlines()
    if tasques:
        print("Llistat de tasques:")
        for tasca in tasques:
            print(tasca.strip())
    else:
        print("El fitxer està buit.\n")

def menu_fitxer():
    while True:
        print("""
        Menú Programa Fitxer:
         1. Inserir element al fitxer
         2. Llistar elements al fitxer
         3. Eliminar un element del fitxer
         4. Modificar un element del fitxer
         5. Sortir
        """)
        op = int(input("Introdueixi una opció del menú: "))
        
        if op == 1:
            tasca = input("Introdueixi la tasca a afegir: ")
            inserir_element(tasca)
        elif op == 2:
            llistar_fitxer()
        elif op == 3:
            tasca = input("Introdueixi la tasca a eliminar: ")
            eliminar_element(tasca)
        elif op == 4:
            antiga = input("Introdueixi la tasca a modificar: ")
            nova = input("Introdueixi la nova tasca: ")
            modificar_element(antiga, nova)
        elif op == 5:
            print("Sortint...")
            break
        else:
            print("Opció no vàlida, torna a intentar-ho.")


    


def pex2():
    crear_fitxer()
    menu_fitxer()

