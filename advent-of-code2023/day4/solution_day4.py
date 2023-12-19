import re
from collections import defaultdict


from utils.utils import get_context_from_file


def get_numbers(_string: str) -> list[int]:
    numbers = list(map(int, re.findall(r"\d+", _string)))
    return numbers


def get_n_winning_numbers(winning_numbers: list[int], your_numbers: list[int]) -> int:
    return len(set(winning_numbers).intersection(set(your_numbers)))


def extract_numbers_from_card(card: str) -> tuple[list[int], list[int]]:
    card, numbers = card.split(":")
    winning_numbers, your_numbers = list(
        map(lambda x: get_numbers(x), numbers.strip().split("|"))
    )
    return winning_numbers, your_numbers


def task_1(lines: list[str]) -> int:
    result = 0
    for line in lines:
        winning_numbers, your_numbers = extract_numbers_from_card(line)
        win = get_n_winning_numbers(winning_numbers, your_numbers)
        result += 2 ** (win - 1) if win > 0 else 0
    return result


def task_2(lines: list[str]) -> int:
    card_copies = defaultdict(lambda: 1)
    for card_index, card in enumerate(lines):
        winning_numbers, your_numbers = extract_numbers_from_card(card)
        win = get_n_winning_numbers(winning_numbers, your_numbers)
        copies = card_copies[card_index]
        for i in range(card_index, card_index + win):
            card_copies[i + 1] += 1 * copies
    return sum(card_copies.values())


if __name__ == "__main__":
    file_context = get_context_from_file("input.txt")
    print(task_1(file_context))
    print(task_2(file_context))
