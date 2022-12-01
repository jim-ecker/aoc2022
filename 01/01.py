'''
Get the top N number of elves calorie totals
inputList: [] : list of calorie totals
n        : int: number of top calorie totals to return

getTopN(inputList, 1) -> get the highest calorie total
getTopN(inputList, 2) -> get the two highest calorie totals
getTopN(inputList, len(inputList)) -> reduces to sum of all calorie totals
'''
def getSumOfTopN(inputList, n):
    try:
        topN = []
        for i in range(n):
            topN.append(inputList.pop(inputList.index(max(inputList)))) # pop the highest calorie total out of inputList and append to topN
        return sum(topN)
    except:
        raise IndexError('n exceeds size of input list')
    
d = []
with open("input.txt") as f:
    for group in f.read().split('\n\n'):
     d.append(sum([int(i) for i in group.split('\n')])) # collapse each elf's snacks to one sum of calories

print('part1: {}'.format(getSumOfTopN(d, 1)))
print('part2: {}'.format(getSumOfTopN(d, 3)))