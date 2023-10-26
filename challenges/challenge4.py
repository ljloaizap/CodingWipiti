'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def is_prime_number(number):
    '''PH'''
    if number < 1:
        return None

    count = 0
    for digit in range(1, number):
        if number % digit == 0:
            count += 1
    return count < 3


def is_fibonacci_number(number):
    '''PH'''
    if number < 0:
        return None
    if number == 0:
        return True

    previous_value = 0
    new_value = 1
    for _ in range(1, number + 1):
        res = new_value + previous_value
        previous_value = new_value
        new_value = res
        if number == res:
            return True
        
    return False


def is_even_number(number):
    '''PH'''
    return number % 2 == 0


def get_info_by_number(number):
    is_prime = ('' if is_prime_number(number) else 'no ') + 'es primo'
    is_fibonacci = ('' if is_fibonacci_number(number) else 'no ') + 'es fibonacci'
    is_even = 'es par' if is_even_number(number) else 'es impar '

    print(f'{number} {is_prime}, {is_fibonacci} y {is_even}.')


if __name__ == "__main__":
    get_info_by_number(2)
    get_info_by_number(7)
