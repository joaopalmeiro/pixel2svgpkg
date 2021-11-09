from pathlib import Path
from typing import List, Tuple, Union

from PIL import Image


# Source: https://stackoverflow.com/a/58541858
def open_image(
    input_path: Union[str, Path]
) -> Tuple[int, int, List[Tuple[int, int, int]]]:
    # More info:
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer
    # - https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getdata
    with Image.open(input_path) as im:
        # print(im.mode)
        im = im.convert("RGBA")

        (width, height) = im.size
        # print(width, height, type(width), type(height))

        rgb_values = list(im.getdata())

    return width, height, rgb_values
