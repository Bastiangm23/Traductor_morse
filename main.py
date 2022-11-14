import Alfabeto

alfabeto = Alfabeto.alfabeto


def traducir(texto_a_traducir):
    for letra in texto_a_traducir.upper():
        print(alfabeto[letra], end=" ")
    print("")


encendido = True


while encendido:
    texto = input("Ingrese el texto a traducir: ")
    if texto == "salir":
        encendido = False
    else:
        traducir(texto)
