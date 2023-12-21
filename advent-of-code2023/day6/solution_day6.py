import math
import re

from utils.utils import get_context_from_file


def extract_numbers_from_line(line: str):
    return list(map(int, re.findall(r"\d+", line)))


def extract_number_from_line(line: str):
    return int(re.sub(r"\s+", "", line).split(":")[1])


def calculate_win(speed: int, time: int, distance: int):
    distance_time = time - speed
    expected_distance = speed * distance_time
    if expected_distance > distance:
        return 1
    return 0


def task_1(lines: list[str]) -> int:
    # puzzle input -> sheet of paper, that lists the time allowed for each race and also the best distance ever recorded in that race.
    # To win grand prize, you need to make sure you go farther in each race than the current record holder.
    # in sample first race: lasts 7 milliseconds, record distance is 9 millimeters
    # Output: determine the number of ways you can beat the record in each race
    times = extract_numbers_from_line(lines[0])
    distances = extract_numbers_from_line(lines[1])
    each_race_wins = []
    for time, distance in zip(times, distances):
        wins = 0
        for hold_time in range(time + 1):
            wins += calculate_win(speed=hold_time, time=time, distance=distance)
        each_race_wins.append(wins)
    return math.prod(each_race_wins)


def task_2(lines: list[str]) -> int:
    time = extract_number_from_line(lines[0])
    distance = extract_number_from_line(lines[1])
    start_hold = 14
    wins = 0
    for hold_time in range(start_hold, time - start_hold + 1):
        wins += calculate_win(hold_time, time, distance)
    return wins


if __name__ == "__main__":
    file_context = get_context_from_file("input.txt")
    print(task_1(file_context))
    print(task_2(file_context))
