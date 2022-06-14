from math import factorial
from random import randint
from supernumbers import NEGATIVE_INFINITE
from typing import List
from time import time


def bogo_sort(array: List[int]):
    """Takes a int list and then tries to sort it by using bogosort, it prints the execution time, the sorted array and the average number of times expected"""
    tempo_antes = time()
    print(array)
    counter = 0
    avg = factorial(len(array))
    try:
        while not is_sorted(array):
            counter += 1
            print(array)
            array = shuffle_array(array)

    except KeyboardInterrupt:
        print()
    finally:
        print(
            f"ARRAY SORTED: {array} TOTAL TIMES: {counter} AVERAGE TIMES EXPECTED: {avg}"
        )
        tempo_depois = time()
        print(f"EXECUTION TIME: {tempo_depois - tempo_antes:.2f}s")
        exit()


def shuffle_array(array: List[int]) -> List[int]:
    """Shuffle an array randomly from given List of integers."""
    length = len(array)
    for i in range(length):
        new_position = randint(0, length - 1)
        aux = array[new_position]
        array[new_position] = array[i]
        array[i] = aux
    return array


def is_sorted(array: List[int]) -> bool:
    """Verify if an given List of integers is sorted or not"""
    anterior = NEGATIVE_INFINITE
    for number in array:
        if number >= anterior:
            anterior = number
        else:
            return False
    return True


def random_array(array_len: int, gap: tuple) -> List[int]:
    """Generate a random List of integers from a given length and range(gap)"""
    array_gerado = []
    for _ in range(array_len):
        array_gerado.append(randint(gap[0], gap[1]))
    return array_gerado

if __name__ == '__main__':
    bogo_sort(random_array(8, (-1000, 1000)))
