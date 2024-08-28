def texto_a_binario(texto):
    return ''.join(format(ord(caracter), '08b') for caracter in texto)

# Solicitar entrada del usuario
texto = input("Introduce el texto que deseas convertir a binario: ")
binario = texto_a_binario(texto)

# Mostrar resultados
print('Texto:', texto)
print('Binario:', binario)