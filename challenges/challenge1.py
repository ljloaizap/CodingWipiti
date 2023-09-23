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


def get_leet_by_character(character: str) -> str:
    '''PH'''
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

    if character in leet:
        return leet[character]
    return character


def main(text):
    '''PH'''
    if text is None:
        return None

    upper_text = text.upper()

    transformed = [get_leet_by_character(char) for char in upper_text]
    new_text = "".join(transformed)
    return new_text
