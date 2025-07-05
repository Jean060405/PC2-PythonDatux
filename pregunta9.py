#pregunta 9
vocales = "aeiouAEIOU"
texto = input("ingrese un texto: ")
sin_vocales = ""

for letra in texto:
    if letra not in vocales:
        sin_vocales += letra

print(sin_vocales)
