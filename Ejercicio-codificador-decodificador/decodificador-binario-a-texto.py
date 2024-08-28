def binario_a_texto(binario):
    texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
    return texto

# Solicitar entrada del usuario
binario = input("Introduce el código binario que deseas convertir a texto: ")

# Asegurarse de que la longitud del binario sea un múltiplo de 8
if len(binario) % 8 != 0:
    print("El código binario debe tener una longitud múltiplo de 8 bits.")
else:
    texto = binario_a_texto(binario)
    print(f'Binario: {binario}')
    print(f'Texto: {texto}')
