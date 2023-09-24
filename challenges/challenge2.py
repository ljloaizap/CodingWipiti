'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
'''


def main(sequence: str) -> str:
    '''PH'''

    if not isinstance(sequence, str):
        print('[Error] La secuencia debe ser un valor de tipo String')
        return 'E-ST'  # Error: String type

    if not sequence:
        print('[Error] La secuencia no puede ser nula ni vacía')
        return 'E-NENV'  # No entry or not valid

    movements = sequence.split(",")
    # if len(movements) == 0:
    #    print('[Error] La secuencia no es válida. Use valores P1/P2 separados por coma')
    #    return 101  # No entry or not valid

    scoring_p1 = 0
    scoring_p2 = 0
    for movement in movements:
        if movement.strip() == 'P1':
            scoring_p1 += 1
        elif movement.strip() == 'P2':
            scoring_p2 += 1
        else:
            print(
                f'[Error] La entrada "{movement}" no es un valor esperado. Debe ser "P1" o "P2"')
            return 'E-NM'  # Non-matching value

        # print_scoring(scoring_p1, scoring_p2)
        print(f'> {get_scoring(scoring_p1, scoring_p2)}')

    return 'I-OK'


def get_scoring(scoring_p1, scoring_p2):
    '''PH'''

    if scoring_p1 == scoring_p2:
        return "Deuce"

    return 'rabbit'


'''
def print_scoring(scoring_p1, scoring_p2):
    scoring = {
        '0': 'Love',
        '1': '15',
        '2': '30',
        '3': '40',
    }

    if scoring_p1 == scoring_p2:
        print("Deuce")
    elif abs(scoring_p1 - scoring_p2) > 1:
        if scoring_p1 > scoring_p2:
            print("Ha ganada el P1")
        else:
            print("Ha ganada el P2")
    elif abs(scoring_p1 - scoring_p2) > 0:
        if scoring_p1 > scoring_p2:
            print("Ventaja P1")
        else:
            print("Ventaja P2")
    else:
        text_p1 = scoring.get(str(scoring_p1), str(scoring_p1))
        text_p2 = scoring.get(str(scoring_p2), str(scoring_p2))
        print(f'{text_p1} - {text_p2}')
'''
