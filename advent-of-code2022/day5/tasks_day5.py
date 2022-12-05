from typing import List
from string import ascii_uppercase
import copy
import re


def open_file():
    with open("input.txt") as file:
        crates, steps = file.read().strip().split('\n\n')

    return crates, steps


def make_crates():
    crates = open_file()[0]
    crates = crates.splitlines()
    crates_numbers = list(crates.pop())
    numbers = []
    for i in range(1, len(crates_numbers), 4):
        numbers.append(crates_numbers[i])
    lista = []
    for i in range(1, 34, 4):
        for crate in crates:
            lista.append(crate[i])

    chunks_crates = [lista[i:i+8] for i in range(0, len(lista), 8)]
    for chunk in chunks_crates:
        while ' ' in chunk:
            chunk.remove(' ')

    return chunks_crates


def task():
    collection = make_crates()
    print(collection)
    for action in open_file()[1].splitlines():
        count, src, dest = map(int, re.findall("\d+", action))
        for _ in range(count):  # Part 1
            collection[dest-1].insert(0, collection[src-1].pop(0))
        # for num in reversed(range(count)):  # Part 2
        #     collection[dest-1].insert(0, collection[src-1].pop(num))
    print(''.join(list(stack[0] for stack in collection)))  # Parts result


task()
