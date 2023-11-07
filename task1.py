def return_prime_numbers(n: int) -> list[int]:
    """
    Функция, возвращающая все простые числа до N

    :param n: последнее число в диапазоне
    :return: список простых чисел
    """
    numbers = list()
    for number in range(1, n + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                numbers.append(number)
    return numbers


print(return_prime_numbers(30))
