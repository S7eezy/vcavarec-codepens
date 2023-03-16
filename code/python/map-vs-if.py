from itertools import cycle
import time

"""
If approach
"""

def ifMethod(mode: str, i: int) -> float:
    if mode == "a":
        return i ** 4
    elif mode == "b":
        return i / 9
    elif mode == "c":
        return i

def ifTest() -> float:
    time_if = time.time()

    for i in range(100000000):
        mode = next(modes)
        ifMethod(mode, i)

    return time.time() - time_if

"""
Map approach
"""

def compute_a(i):
    return i ** 4

def compute_b(i):
    return i / 9

def compute_c(i):
    return i

def mapMethod(mode: str, i: int) -> float:
    return modes_map[mode](i)

def mapTest() -> float:
    time_map = time.time()

    for i in range(100000000):
        mode = next(modes)
        mapMethod(mode, i)

    return time.time() - time_map


if __name__ == "__main__":

    modes = cycle(["a", "b", "c"])

    modes_map = {"a": compute_a, "b": compute_b, "c": compute_c}

    print(f"If method: {ifTest()}")

    print(f"Map method: {mapTest()}")

