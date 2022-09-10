

def validar(usuario):
    if usuario.isalnum()==False:
        print("El usuario solo debe contener letras y numeros ")
    elif 6 > len(usuario):
        print("El nombre de usuario debe contener un minimo de 6 caracteres")     
    elif 12 < len(usuario):
        print("El nombre no debe de contener mayor a 12 caracteres")
    elif 6 <= len(usuario) <=12:
        print("Nombre de usuario valido :)")
    return

def validarContraseña(contraseña):
    if 8 > len(contraseña):
        print("La contraseña debe contener un maximo de 8 caracteres") 
    elif contraseña.count(" ")>0:
        print("La contraseña no debe tener espacios en blancos")

    elif 8 == len(contraseña):
        print("Contraseña valida :)") 

    return