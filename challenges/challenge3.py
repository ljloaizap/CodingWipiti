'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''

import random
import string


def main(length=16, with_mayus=True, with_numbers=True, with_symbols=True):
    '''PH'''

    if length < 8 or length > 16:
        return "[Err] La longitud debe estar entre 8 y 16"

    letters = string.ascii_letters if with_mayus else string.ascii_lowercase
    if with_numbers:
        letters += string.digits
    if with_symbols:
        letters += string.punctuation

    return ''.join(random.choice(letters) for _ in range(length))


print(main(with_numbers=True))
