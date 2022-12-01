def getTopN(inputList, n):
    topN = []
    for i in range(n):
        topN.append(inputList.pop(inputList.index(max(inputList))))
    return topN
    
d = []
with open("input.txt") as f:
    for group in f.read().split('\n\n'):
     d.append(sum([int(i) for i in group.split('\n')]))

print('part1: {}'.format(sum(getTopN(d, 1))))
print('part2: {}'.format(sum(getTopN(d, 3))))