import re
from itertools import chain
from operator import itemgetter
from pathlib import Path
from typing import List

from utils.utils import get_context_from_file, timeit


@timeit
def task_1(lines: List[str]):
    digits_from_line = [list(filter(lambda x: x.isdigit(), line)) for line in lines]
    two_digits_group = [
        [int(digit[0] + digit[-1])]
        if len(digit) >= 2
        else list(map(lambda x: int(x), list(map(lambda x: x * 2, digit))))
        if len(digit) == 1
        else digit
        for digit in digits_from_line
    ]
    return sum(list(chain(*two_digits_group)))


@timeit
def task_2(lines: List[str]):
    digits_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    numbers = []
    ## znalezienie wszystkich cyfr + ich indeksy potem posortowanie ich
    for line in lines:
        values_with_indexes = [
            [match.start(), int(match.group())] for match in re.finditer(r"\d", line)
        ]
        for key, value in digits_map.items():
            values_with_indexes.extend(
                [match.start(), value] for match in re.finditer(key, line)
            )
        sorted_values_with_indexes = sorted(values_with_indexes, key=itemgetter(0))
        number_to_pick = str(sorted_values_with_indexes[0][1]) + str(
            sorted_values_with_indexes[-1][1]
        )
        numbers.append(int(number_to_pick))
    return sum(numbers)


if __name__ == "__main__":
    input_path = Path.cwd() / "input.txt"
    file_context = get_context_from_file(input_path)
    # print(task_1(file_context))
    print(task_2(file_context))
