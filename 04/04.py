def parse_pairs(pairs: list) -> tuple:
    return pairs[0].split('-'), pairs[1].split('-')


def get_sets(a: list, b: list) -> tuple:
    """
    Converts a range of numbers into a set of all the integers in that range
    :param a: first pair range [low, high]
    :param b: second pair range [low, high]
    :return: tuple containing sets of numbers for given ranges
    """
    a = set(range(int(a[0]), int(a[1]) + 1))
    b = set(range(int(b[0]), int(b[1]) + 1))
    return a, b


d = []
with open("input.txt") as f:
    for group in f.read().split('\n'):
        d.append(group)
count = 0
overlap = 0
for item in d:
    pair1, pair2 = parse_pairs(item.split(','))
    pair1, pair2 = get_sets(pair1, pair2)
    if pair1 == pair2:
        count += 1
    elif pair1.issubset(pair2):
        count += 1
    elif pair2.issubset(pair1):
        count += 1
    elif not pair1.isdisjoint(pair2):
        overlap += 1
print('part 1: {}'.format(count))
print('part 1: {}'.format(count + overlap))


