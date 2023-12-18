import re
from collections import defaultdict
from pathlib import Path
from re import Match
from typing import Any, Union

from utils.utils import get_context_from_file, timeit


def take_lines_to_search(lines: list[str]) -> list[list[Union[str, Match[str], Any]]]:
    _LAST_LINE = len(lines) - 1
    lines_to_search = []

    for index_line, line in enumerate(lines):
        _END_OF_LINE = len(line) - 1
        for match in re.finditer(r"\d+", line.strip()):
            start_substring = match.start() - 1 if match.start() > 0 else 0
            end_substring = (
                match.end() + 1 if match.end() < _END_OF_LINE else _END_OF_LINE
            )
            number_to_check = line[start_substring:end_substring]
            y_down = index_line - 1 if index_line > 0 else 0  # range [- infinity;0 ]
            y_up = (
                index_line + 1 if index_line < _LAST_LINE else _LAST_LINE
            )  # range [0; infinity]
            line_to_search = (
                lines[y_up][start_substring:end_substring]
                + lines[y_down][start_substring:end_substring]
                + number_to_check
            )
            lines_to_search.append([line_to_search, match])
    return lines_to_search


@timeit
def task_1(lines) -> int:
    special_characters = r"[!@#$%^&*()\-+?_=,<>/]"
    result = 0
    regex = re.compile(special_characters)
    for line_to_search, match in lines:
        if regex.search(line_to_search) is not None:
            result += int(match.group())
    return result


def find_adjacent_gears(
    start_match: int,
    end_match: int,
    end_of_line: int,
    index_line: int,
    last_line: int,
    line: str,
    lines: list[str],
) -> list[tuple[int, int]]:
    gears = []
    start_substring = start_match - 1 if start_match > 0 else 0
    end_substring = end_match + 1 if end_match < end_of_line else end_of_line
    y_down = index_line - 1 if index_line > 0 else 0  # range [- infinity;0 ]
    y_up = (
        index_line + 1 if index_line < last_line else last_line
    )  # range [0; infinity]
    if "*" in lines[y_up][start_substring:end_substring]:
        gear_index = lines[y_up].index("*", start_substring)
        gears.append((y_up, gear_index))
    elif "*" in lines[y_down][start_substring:end_substring]:
        gear_index = lines[y_down].index("*", start_substring)
        gears.append((y_down, gear_index))
    elif "*" in line[start_substring:end_substring]:
        gear_index = lines[index_line].index("*", start_substring)
        gears.append((index_line, gear_index))
    return gears


def task_2(lines: list[str]) -> int:
    _LAST_LINE = len(lines) - 1
    _NUMBERS_PATTERN = r"\d+"
    gears = defaultdict(list)
    result = 0
    # Gear -> any "*" symbol that is adjacent to exactly two part number
    # Find the gear ratio of every gear and add them all
    for index_line, line in enumerate(lines):
        _END_OF_LINE = len(line) - 1
        for match in re.finditer(_NUMBERS_PATTERN, line.strip()):
            found_gears = find_adjacent_gears(
                match.start(),
                match.end(),
                _END_OF_LINE,
                index_line,
                _LAST_LINE,
                line,
                lines,
            )
            for gear in found_gears:
                gears[gear].append(int(match.group()))
    for key, value in gears.items():
        if len(value) == 2:
            result += value[0] * value[1]

    return result


if __name__ == "__main__":
    filepath = Path.cwd() / "input.txt"
    file_context = get_context_from_file(filepath)
    lines_to_search = take_lines_to_search(file_context)
    print(task_1(lines_to_search))
    print(task_2(file_context))
