from collections import defaultdict


def print_stacks(stacks: defaultdict):
    """
    Prints a visual representation of the stacks of crates, transposed
    :param stacks: defaultdict: current state of the stacks
    """
    for row in range(len(stacks.keys())):
        print('{}: {}'.format(row, str(stacks[row])))


def get_answer(stacks: defaultdict) -> str:
    """
    Builds a string representing the top crates on each stack
    :param stacks: defaultdict: current state of the stacks
    :return: string listing the top crates on the stacks
    """
    answer = ''
    for row in range(len(stacks.keys())):
        if len(stacks[row]) > 0:
            answer += stacks[row][0]
    return answer


def do_work(plan: list, stacks: defaultdict, batch:bool = False):
    """
    Executes the move plan given in the input
    :param plan: the full plan of all the moves needed
    :param stacks: current state of the stacks
    :param batch: True if we can pick up a stack of crates from the stack, False if we can only pick one stack up at a time
    """
    for move in plan:
        if batch:
            package = []
        for moves in range(move['move']):
            if len(stacks[move['from'] - 1]) > 0:
                if batch:
                    package.append(stacks[move['from'] - 1].pop(0))
                else:
                    stacks[move['to'] - 1].insert(0, stacks[move['from'] - 1].pop(0))
        if batch:
            for crate in range(len(package)):
                stacks[move['to'] - 1].insert(0, package.pop())


def parse_moves(moves: list) -> list:
    """
    Builds a list of moves parsed from the input string
    :param moves: list of strings representing moves we need to do
    :return: list of dictionaries representing each move
    """
    plan = []
    for move in moves:
        move = move.split(" ")
        plan.append(
            {
                move[0]: int(move[1]),
                move[2]: int(move[3]),
                move[4]: int(move[5])
            }
        )
    return plan


def reset() -> tuple:
    """
    Resets the state of the stacks to the original state given by the input
    :return: tuple of (stacks, moves)
    """
    with open("input.txt") as f:
        game = [next(f) for x in range(8)]
    stacks = defaultdict(list)
    for level in game:
        level = str(level)
        stacks[0].append(level[1])
        for elem in range(2, len(level)):
            if level[elem].isalpha():
                stacks[elem // 4].append(level[elem])

    moves = []
    with open("input.txt") as f:
        for move in f.read().split('\n'):
            moves.append(move)
    moves = parse_moves(moves[10:])

    return stacks, moves


stacks, moves = reset()
do_work(moves, stacks)
print('part 1: {}'.format(get_answer(stacks)))

stacks, moves = reset()
do_work(moves, stacks, batch=True)
print('part 2: {}'.format(get_answer(stacks)))

