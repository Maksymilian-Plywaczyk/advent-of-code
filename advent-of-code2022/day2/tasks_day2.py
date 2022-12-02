

def open_file(path: str):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [x.rstrip('\n') for x in lines]
    return lines


def task1():
    # First column:
    # A -> rock 1 points
    # B -> paper 2 points
    # C -> Scissors 3 points

    # Win 6 points
    # Draw 3 poins
    # Lost 0 points

    # Second column:
    # X -> rock
    # Y -> paper
    # Z -> Scissors
    opts = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6}
    rounds = open_file("input.txt")
    return sum(opts.get(key) for key in rounds if key in opts.keys())


def task2():
    # Y -> draw
    # X -> lose
    # Z -> win
    opts = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7}
    rounds = open_file("input.txt")
    return sum(opts.get(key) for key in rounds if key in opts.keys())


print(task1())
print(task2())
