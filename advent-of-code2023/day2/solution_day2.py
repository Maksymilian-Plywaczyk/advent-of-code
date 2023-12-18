import operator
from functools import reduce
from pathlib import Path

from utils.utils import get_context_from_file, timeit


@timeit
def task_1(lines: list[str]) -> int:
    _MAX_RED = 12
    _MAX_GREEN = 13
    _MAX_BLUE = 14
    result = 0
    for line in lines:
        bag_info = {"red": 0, "blue": 0, "green": 0}
        row = line.split(" ")
        game_index = row[1].removesuffix(":")
        sets = row[2:]
        for index, element in enumerate(sets):
            if index % 2 == 0:
                color = sets[index + 1].replace(";", "").replace(",", "")
                bag_info[color] = max(bag_info[color], int(element))
        if (
            bag_info["red"] <= _MAX_RED
            and bag_info["green"] <= _MAX_GREEN
            and bag_info["blue"] <= _MAX_BLUE
        ):
            result += int(game_index)
    return result


@timeit
def task_2(lines: list[str]) -> int:
    powers_sum = 0
    for line in lines:
        bag_info = {"red": 0, "blue": 0, "green": 0}
        row = line.split(" ")[2:]
        for index, element in enumerate(row):
            if index % 2 == 0:
                color = row[index + 1].replace(";", "").replace(",", "")
                bag_info[color] = max(bag_info[color], int(element))
        powers_sum += reduce(operator.mul, bag_info.values())
    return powers_sum


if __name__ == "__main__":
    filepath = Path.cwd() / "input.txt"
    file_context = get_context_from_file(filepath)
    task_1(file_context)
    task_2(file_context)
