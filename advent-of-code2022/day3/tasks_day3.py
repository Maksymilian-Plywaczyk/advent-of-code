from typing import List


def open_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        lines = file.readlines()

    return [x.rstrip('\n') for x in lines]


def priority_check(letter: str) -> int:

    if letter.islower():
        # ord() -> integer representing the Unicode character a= 97, A=65
        piority = ord(letter)-96
    elif letter.isupper():
        piority = ord(letter) - 38
    return piority


def task1():

    rucksacks = open_file("input.txt")
    priority_sum = 0

    for rucksack in rucksacks:
        first_compartment = rucksack[0:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]
        common_character = ''.join(
            set(first_compartment).intersection(second_compartment))
        priority_sum += priority_check(common_character)

    print(f"Sum of piority: {priority_sum} ")


def task2():
    rucksacks = open_file("input.txt")
    priority_sum = 0

    for group_rucksacks in range(0, len(rucksacks), 3):
        group = rucksacks[group_rucksacks:group_rucksacks+3]
        common_character = ''.join(
            set(group[0]).intersection(group[1], group[2]))
        priority_sum += priority_check(common_character)
    print(f"Sum of groups piority: {priority_sum} ")


task1()
task2()
