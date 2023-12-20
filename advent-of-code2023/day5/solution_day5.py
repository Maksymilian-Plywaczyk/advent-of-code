from utils.utils import get_context_from_file
from typing import NamedTuple
import re


class Ranges(NamedTuple):
    destination_range_start: int
    source_range_start: int
    range_length: int

    def __repr__(self):
        return f"Range destination start {self.destination_range_start}, source start: {self.source_range_start}, length: {self.range_length}"


def get_planted_seeds(file_input: list[str]) -> tuple[int, ...]:
    seeds = tuple(
        map(int, list(filter(lambda x: x.isnumeric(), file_input[0].split(" "))))
    )
    return seeds


def get_ranges_from_line(line: str):
    pattern = r"(\d+ \d+ \d+)"
    match = re.search(pattern, line)
    if match is not None:
        return tuple(map(int, match.group().split(" ")))


def transform_to_range(ranges_numbers: list[tuple[int, int, int]]):
    ranges = [Ranges(*range) for range in ranges_numbers]
    return ranges


def get_new_numbers(ranges: list[Ranges], seeds: tuple[int, ...]):
    def map_new_numbers(seed: int):
        for _range in ranges:
            print(seed, _range)
            if (
                _range.source_range_start
                <= seed
                <= (_range.source_range_start + _range.range_length)
            ):
                new_number = (
                    _range.destination_range_start + seed - _range.source_range_start
                )
                return new_number
        return seed

    new_numbers = []
    for seed in seeds:
        new_numbers.append(map_new_numbers(seed))
    return new_numbers


def task_1(lines: list[str]) -> list[int]:
    # Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
    # Range length determinate how many steps we can move from destination range start and the source range start example: 50, 80, 3 it will
    # The destination start from 50 ends to 52, source range start from 80 ends to 82, end 50=80,51=82,52=82
    _seeds = get_planted_seeds(lines)
    numbers = _seeds
    for line in lines[1:]:
        ranges_numbers = list(
            filter(
                lambda x: x is not None,
                list(map(lambda x: get_ranges_from_line(x), line.split("\n"))),
            )
        )
        ranges = transform_to_range(ranges_numbers)
        numbers = get_new_numbers(ranges, numbers)
    return numbers


if __name__ == "__main__":
    file_context = get_context_from_file("input.txt", True)
    print(min(task_1(file_context)))
