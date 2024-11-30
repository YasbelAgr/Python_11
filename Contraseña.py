
import re
contraseña = input("Introduce una contraseña: ")

if (len(contraseña) >=8 and
    re.search(r"[A-Z]", contraseña) and
    re.search(r"[a-z]", contraseña)and
    re.search(r"\d", contraseña)):
    print("La contraseña es valida")
else:
    print("La contraseña no es valida")

