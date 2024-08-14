Users = {

}

def NuevoUsuario():
    username = str(input("A continuacion ingrese un nombre de usuario: "))
    while username.isspace() == True or username =="": #Este programa tiene como agregado el uso de isspace y comprueba si es unicamente un espacio en blanco, ya que si un usuario utilizara Espacios unicamente le permitiria crear un usuario en blanco
        print("Su usuario no puede estar vacio ")
        username = str(input("A continuacion ingrese un nombre de usuario: "))
    else: pass
    password = str(input("A continuacion ingrese la contraseña para este usuario: "))
    while password.isspace() == True or password == "":
        print("Su contraseña no puede estar vacia ")
        password = str(input("A continuacion ingrese la contraseña para este usuario: "))
    else: pass
    print("Usuario Registrado correctamente")
    Users[username] = password



def MostrarUsuarios():
    print("El o los diferentes usuarios que estan registrados en el sistema son:")
    print(f"{Users}")


def login():
    while True:
            nombredeusuario = str(input("Ingrese su usuario: "))
            while nombredeusuario.isspace() == True or nombredeusuario =="":
                 print("No existe un usuario vacio")
                 nombredeusuario = str(input("Ingrese su usuario: "))
            else: pass
            contraseña = str(input("Ingrese su contraseña: "))

            if nombredeusuario in Users:
                if Users[nombredeusuario] == contraseña:
                    print(f"Bienvenido al sistema {nombredeusuario}")
                    break
                else:
                    print("Contraseña Incorrecta, intentelo nuevamente")
            else:
                 print("Este usuario no se encuentra registrado en el sistema")
                 break
