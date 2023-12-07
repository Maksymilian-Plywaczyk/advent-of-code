import re
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


def task_2(lines: list[str]):
    # Work in progress
    for index, (line_to_search, match) in enumerate(lines):
        if "*" in line_to_search:
            print(index, line_to_search, match.group())


if __name__ == "__main__":
    filepath = Path.cwd() / "input.txt"
    file_context = get_context_from_file(filepath)
    lines_to_search = take_lines_to_search(file_context)
    # print(task_1(lines_to_search))
    task_2(lines_to_search)
