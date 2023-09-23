'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''


def main(text):
    '''PH'''

    if text is None:
        return None

    leet = {
        'A': '4',
        'B': 'I3',
        'C': '[',
        'D': ')',
        'E': '3',
        'F': '|=',
        'G': '&',
        'H': '#',
        'I': '1',
        'J': ',_|',
        'K': '>|',
        'L': '1',
        'M': r'/\/\\',
        'N': '^/',
        'O': '0',
        'P': '|*',
        'Q': '(_,)',
        'R': 'I2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': r'\/',
        'W': r'\/\/',
        'X': '><',
        'Y': 'j',
        'Z': '2'
    }

    return "".join([leet.get(char, char) for char in text.upper()])
