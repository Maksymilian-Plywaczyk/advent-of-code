
from typing import List


def open_file(path: str):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [x.rstrip('\n') for x in lines]
    return lines


def task_1() -> List[int]:
    accumulator = 0
    elvs_results = []

    for line in open_file("input.txt"):
        if line == '':
            elvs_results.append(accumulator)
            accumulator = 0
        else:
            accumulator += int(line)

    print(f"Elve with the most calories: {max(elvs_results)}")
    return elvs_results


def task_2():
    elvs_calories = task_1()
    elvs_calories = sum((sorted(elvs_calories, reverse=True)[0:3]))
    print(f"Top three elvs sum of calories: {elvs_calories}")

#66306, 64532, 64454


task_2()
