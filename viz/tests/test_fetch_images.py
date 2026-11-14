from PIL import Image

from viz.scripts.fetch_images import is_usable_image


def test_image_acceptance_rejects_invisible_and_white_only_images():
    transparent = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    white_logo = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    white_logo.paste((255, 255, 255, 255), (16, 16, 48, 48))
    black_logo = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    black_logo.putpixel((32, 32), (0, 0, 0, 255))
    photo = Image.new("RGB", (64, 64))
    photo.putdata([(x * 4, y * 4, (x + y) * 2) for y in range(64) for x in range(64)])

    assert not is_usable_image(transparent)
    assert not is_usable_image(white_logo)
    assert is_usable_image(black_logo)
    assert is_usable_image(photo)
