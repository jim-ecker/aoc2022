def traverse_window(signal: str, N: int) -> str:
    """
    Runs two pointers over str. First pointer is beginning of window of size N, second is a runner to read next N chars
    The window slides over the string until it finds a window with all distinct characters
    :param signal: String to slide window over
    :param N: Size of window
    :return: substring of size N with distinct characters
    """
    for i in range(len(signal) - N + 1):
        window = []
        for runner in range(N):
            window.append(signal[i+runner])
        if len(window) == len(set(window)): # list contains all distinct chars
            substring = ''
            for x in window:
                substring += x
            return substring


d = []
with open("input.txt") as f:
    for line in f.read().split('\n'):
        d.append(line)

signal = d[0]
target = traverse_window(signal, 4)
elem = d[0].find(target)
print('part 1: {}'.format(elem + 4))

target = traverse_window(signal, 14)
elem = d[0].find(target)
print('part 2: {}'.format(elem + 14))


