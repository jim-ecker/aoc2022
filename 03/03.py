d = []
with open("input.txt") as f:
    for group in f.read().split('\n'):
        d.append(group.split())

print(d)
