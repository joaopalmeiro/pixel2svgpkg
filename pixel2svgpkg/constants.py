from typing import List, NamedTuple, Tuple

DEFAULT_SQUARE_SIZE: int = 1  # px


# More info:
# - https://docs.python.org/3.6/library/typing.html#typing.NamedTuple
# - https://stackoverflow.com/a/44833864
class RGBImage(NamedTuple):
    width: int
    height: int
    values: List[Tuple[int, int, int, int]]  # RGBA
