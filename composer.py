import os
from PIL import Image, ImageDraw, ImageFont
from collector import collect

img_width = 0
img_height = 0


def get_font(size=20):
    paths = [
        "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/TTF/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/liberation-mono-fonts/LiberationMono-Regular.ttf",
    ]
    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def create_base(width=1280, height=720, bg_color="#fffced"):
    global img_width, img_height
    img_width = width
    img_height = height
    base = Image.new("RGB", (width, height), color=bg_color)
    return base


def paste_screenshot(base, image_path):
    new_width = int(img_width / 2)
    new_height = int(img_height / 2)
    img = Image.open(image_path)
    resize_image = img.resize((new_width, new_height))
    base.paste(resize_image, (int(img_width * 0.05), int(img_height * 0.25)))
    return base


def draw_info(base):
    font = get_font(20)

    color = "#263A43"

    draw = ImageDraw.Draw(base)

    x = int(img_width * 0.65)
    y = int(img_height / 2)
    line_height = 20

    info_dictionary = collect()

    draw.text(
        (int(img_width * 0.05), int(img_height * 0.1)),
        "MY RICE CARD",
        fill=color,
        font=get_font(60),
    )

    for key, value in info_dictionary.items():
        if isinstance(value, list):
            for i in value:
                draw.text((x, y), f"{key}: {i}", fill=color, font=font)
                y += line_height
        else:
            draw.text((x, y), f"{key}: {value}", fill=color, font=font)
            y += line_height

    return base


def draw_seal(base, seal_path=None, stamp_path=None):
    if seal_path and stamp_path:
        seal = Image.open(seal_path).convert("RGBA")
        stamp = Image.open(stamp_path).convert("RGBA")
        rotated_stamp = stamp.rotate(45, expand=True)
        base.paste(
            seal,
            ((int(img_width * 0.80)), int(img_height * 0.02)),
            mask=seal.split()[3],
        )
        base.paste(
            rotated_stamp,
            ((int(img_width * 0.65)), int(img_height * 0.05)),
            mask=rotated_stamp.split()[3],
        )
        return base

    return base


def draw_decoration(base):

    draw = ImageDraw.Draw(base)

    color = "#C93F2B"

    # draw thumbnail line
    draw.line(
        [(img_width * 0.60, img_height), (img_width * 0.60, 0)], fill=color, width=5
    )

    # draw information line
    draw.line(
        [(img_width * 0.65, img_height * 0.45), (img_width * 0.90, img_height * 0.45)],
        fill=color,
        width=5,
    )

    return base


def compose(
    image_path, seal_path=None, stamp_path=None, output_path=None, display_name=None
):
    base = create_base()
    base = paste_screenshot(base, image_path)
    base = draw_info(base)
    base = draw_seal(base, seal_path, stamp_path)
    base = draw_decoration(base)
    output = output_path or os.path.expanduser("~/Downloads/rice-card.png")
    base.save(output)
    base.show()
    print(f"Card saved to {output}")
