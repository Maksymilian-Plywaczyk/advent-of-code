from utils.utils import get_context_from_file
from typing import NamedTuple, Any
import re


class MapSeeds(NamedTuple):
    start_range: int
    length_range: int

    def __repr__(self):
        return f"Range start {self.start_range}, length: {self.length_range}"


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


def chunk_seeds_to_pairs(seeds: tuple[int, ...], N=2):
    return [MapSeeds(*seeds[i : i + N]) for i in range(0, len(seeds) - 1, N)]


def get_new_seeds(seed: MapSeeds) -> list[int]:
    return [
        seed for seed in range(seed.start_range, seed.length_range + seed.start_range)
    ]


def task_1(lines: list[str]) -> int:
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
    return min(numbers)


def task_2(lines: list[str]):
    # Seeds line describes ranges of seed numbers. Seeds come in pairs, first number of pair is start of the range second is the length of
    # the range.
    _seeds = get_planted_seeds(lines)
    _seeds = chunk_seeds_to_pairs(_seeds)
    results = []
    for seed in _seeds:
        seeds = tuple(get_new_seeds(seed))
        for line in lines[1:]:
            ranges_numbers = list(
                filter(
                    lambda x: x is not None,
                    list(map(lambda x: get_ranges_from_line(x), line.split("\n"))),
                )
            )
            ranges = transform_to_range(ranges_numbers)
            numbers = get_new_numbers(ranges, seeds)
            results.append(min(numbers))
        results = [min(results)]
    return results[0]


if __name__ == "__main__":
    file_context = get_context_from_file("input.txt", True)
    print(task_1(file_context))
    print(task_2(file_context))
