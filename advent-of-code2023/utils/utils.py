import time
from functools import wraps
from pathlib import Path
from typing import Callable, List


def timeit(func: Callable):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def get_context_from_file(filename: str, split_by_empty_line: bool = False) -> List[str]:
    filename_path = Path.cwd() / filename
    try:
        with open(filename_path, "r") as file:
            if split_by_empty_line:
                return file.read().split("\n\n")
            return file.read().splitlines()
    except (FileExistsError, FileNotFoundError) as e:
        raise e
