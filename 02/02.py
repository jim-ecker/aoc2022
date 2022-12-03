'''
calculateScore(game, rules)
calculates the final score for a sequence of games based on the given ruleset

games: []   : list of games,  [0]: opponent action [1] player action
rules: {}   : ruleset for the given list of games. This is a mapping of actions to score for each game

return: int : the total score for the given sequence of games
'''


def calculateScore(games: list, rules: dict) -> int:
    scores = []
    for game in games:
        scores.append(rules.get(game[0], {}).get(game[1]))
    return sum(scores)


games = []
with open("input.txt") as f:
    for group in f.read().split('\n'):
        games.append(group.split())

partRules = {
    1: {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}},
    2: {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}
}
print('part1: {}'.format(calculateScore(games, partRules.get(1))))
print('part2: {}'.format(calculateScore(games, partRules.get(2))))
