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

    scoring = {
        '0': 'Love',
        '1': '15',
        '2': '30',
        '3': '40',
    }

    scoring_p1 = 0
    scoring_p2 = 0
    movements = sequence.split(",")
    print(f'> Secuencia: {sequence}')

    for movement in movements:
        if movement.strip() == 'P1':
            scoring_p1 += 1
        elif movement.strip() == 'P2':
            scoring_p2 += 1
        else:
            print(
                f'[Error] La entrada "{movement}" no es un valor esperado. Debe ser "P1" o "P2"')
            return 'E-NM'  # Non-matching value

        if scoring_p1 == scoring_p2:
            print('Deuce')
        elif scoring_p1 < 4 and scoring_p2 < 4:
            print(f'{scoring.get(str(scoring_p1))} - {scoring.get(str(scoring_p2))}')
        else:
            diff = scoring_p1 - scoring_p2
            if diff == 1:
                print('Ventaja P1')
            elif diff == -1:
                print('Ventaja P2')
            elif diff > 1:
                print('Ha ganado el P1')
                break
            elif diff < -1:
                print('Ha ganado el P2')
                break
            else:
                print('El programa no sabe / no responde')

    return 'I-OK'


# print(main('P1, P1, P1, P1, P1, P1, P1, P1'))
print(main('P1, P1, P1, P2, P2, P2, P1, P1'))
