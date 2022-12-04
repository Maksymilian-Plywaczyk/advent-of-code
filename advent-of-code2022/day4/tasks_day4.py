from typing import List


def open_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        lines = file.readlines()

    return [x.rstrip('\n') for x in lines]


def tasks_1_2():
    fully_contains = 0
    fully_contains_task2 = 0
    elvs_pairs = open_file("input.txt")

    for pair in elvs_pairs:
        first_pair1, first_pair2, second_pair1, second_pair2 = ' '.join(
            ' '.join(pair.split(',')).split('-')).split()

        if int(first_pair1) <= int(second_pair1) and int(first_pair2) >= int(second_pair2) or int(second_pair1) <= int(first_pair1) and int(second_pair2) >= int(first_pair2):
            fully_contains += 1

        if not (int(first_pair2) < int(second_pair1) or int(second_pair2) < int(first_pair1)):
            fully_contains_task2 += 1
    print(fully_contains)
    print(fully_contains_task2)


tasks_1_2()
