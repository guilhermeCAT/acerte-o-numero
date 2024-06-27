numero = input("escolha um numero: ")
numero_int= int(numero)

contador = 1

while contador < numero_int:
    print(f'numero invalido: {contador}')
    contador += 1

    if numero_int == contador:
        print(f'esse foi seu numero: {contador}')
        break