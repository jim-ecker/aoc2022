import string
from itertools import zip_longest


def intersection_of_sets(data: list) -> set:
    """
    For n sized arbitrary list data = [0, 1, 2 ... n-2, n-1, n],
        calculates the intersection of all elements of the list, where each element is treated as a set
    :param data: list of sets to intersect
    :return: set containing the intersection of the sets.
    """
    sets = map(set, data)
    return set.intersection(*sets)


def get_common(data: list, n: int = 2, priority: list = string.ascii_letters) -> int:
    """
    calculates the priority sum of common elements between n-sized groups of elements of list
    :param data: list to calculate over
    :param n: size of groups in which to find common elements
    :param priority: mapping of elements to an integer representing its importance
    :return: the priority sum of the common elements
    """
    answer = 0
    for item in zip_longest(*[iter(data)] * n, fillvalue=''):
        for letter in intersection_of_sets(list(item)):
            answer += priority.index(letter) + 1
    return answer


def split_string_in_half(istring: str) -> tuple:
    """
    splits a string half
    :param istring: the string to split
    :return: a tuple containing each half of the original string
    """
    return istring[:len(istring) // 2], istring[len(istring) // 2:]


def process_for_part_1(data: list) -> list:
    """
    Part 1 specifies that the string for each knapsack inventory needs to be split in half
    this function processes the original data so that each knapsack is split in half
    :param data: the original data
    :return: a list containing each string in the original data split apart
    """
    processed = []
    for item in data:
        for part in split_string_in_half(item):
            processed.append(part)
    return processed


d = []
with open("input.txt") as f:
    for group in f.read().split('\n'):
        d.append(group)

print(d)
print('part1: {}'.format(get_common(process_for_part_1(d), 2)))
print('part2: {}'.format(get_common(d, 3)))


