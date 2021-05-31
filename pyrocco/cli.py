from math import ceil

import pkg_resources
from PIL import Image

from .constants import DELAY, MEGA_PATH


def layer_images(background, foreground):
    canvas = Image.new("RGBA", background.size, color=(0, 0, 0, 0))
    offset = background.size[1] - foreground.size[1]

    canvas.paste(background, (0, 0), background)
    canvas.paste(foreground, (0, offset), foreground)

    return canvas


def main():
    frames = sorted(pkg_resources.resource_listdir(__name__, MEGA_PATH))
    imgs = [
        Image.open(pkg_resources.resource_stream(__name__, f"{MEGA_PATH}/{frame}"))
        for frame in frames
    ]

    background = Image.open("logo.png")

    thumbnail_size = (
        imgs[0].size[0],
        ceil(imgs[0].size[0] * background.size[1] / background.size[0]),
    )  # Figma: ceil

    background.thumbnail(
        (max(thumbnail_size), max(thumbnail_size)), Image.LANCZOS
    )  # `thumbnail`: floor

    # offset = background.size[1] - imgs[0].size[1]

    to_gif = [layer_images(background, img) for img in imgs]

    to_gif[0].save(
        "mega.gif",
        format="GIF",
        append_images=to_gif[1:],
        save_all=True,
        duration=DELAY,
        loop=0,
        optimize=False,
        transparency=255,
        disposal=2,
    )


if __name__ == "__main__":
    main()
