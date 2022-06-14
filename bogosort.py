from math import factorial
from random import randint
from supernumbers import NEGATIVE_INFINITE
from typing import List
from time import time


def bogo_sort(array: List[int]):
    """Takes a int list and then tries to sort it by using bogosort, it prints the execution time, the sorted array and the average number of times expected"""
    pre_time = time()
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
        pos_time = time()
        print(f"EXECUTION TIME: {pos_time - pre_time:.2f}s")
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
    pre_num = NEGATIVE_INFINITE
    for number in array:
        if number >= pre_num:
            pre_num = number
        else:
            return False
    return True


def random_array(array_len: int, gap: tuple) -> List[int]:
    """Generate a random List of integers from a given length and range(gap)"""
    generated_arr = []
    for _ in range(array_len):
        generated_arr.append(randint(gap[0], gap[1]))
    return generated_arr

if __name__ == '__main__':
    bogo_sort(random_array(8, (-1000, 1000)))
