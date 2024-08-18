Users = {

}

def NuevoUsuario():
    username = str(input("A continuacion ingrese un nombre de usuario: "))
    if username in Users:
        print("Este usuario ya existe")
    else:
        while (username == "") or (" " in username):
            print("Su usuario no puede estar vacio o contener espacios ")
            username = str(input("A continuacion ingrese un nombre de usuario: "))
        else: pass
        password = str(input("A continuacion ingrese la contraseña para este usuario: "))
        while (password == "") or (" " in password):
            print("Su contraseña no puede estar vacia o contener espacios ")
            password = str(input("A continuacion ingrese la contraseña para este usuario: "))
        else:
            if password == username:
                print("Su Contraseña no puede ser igual al usuario")
            else:
                print("Usuario Registrado correctamente")
        Users[username] = password



def MostrarUsuarios():
    print("El o los diferentes usuarios que estan registrados en el sistema son:")
    print(f"{Users}")


def login():
    while True:
            nombredeusuario = str(input("Ingrese su usuario: "))
            while (nombredeusuario == "") or (" " in nombredeusuario):
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
