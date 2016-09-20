import os
tipo = raw_input("Ingrese el tipo: ")
msj = raw_input("Ingrese el mensaje: ")
os.system('git add .')
os.system("""git commit -am '{"responsable": "Hebert Romero","tipo": "%s", "msj": "%s"}' """ %(tipo,msj))