#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
from collections import namedtuple

def create_banner_with_transparent_bg(bg_path, profile):
    # Load the background image and make it half transparent
    bg_image = Image.open(bg_path).convert("RGBA")
    for x in range(bg_image.width):
        for y in range(bg_image.height):
            r, g, b, a = bg_image.getpixel((x, y))
            bg_image.putpixel((x, y), (r, g, b, 128))  # Setting alpha to 128 for half transparency

    banner = bg_image
    
    # Draw text on the banner
    draw = ImageDraw.Draw(banner)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to DejaVuSans-Bold font on Ubuntu
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    
    y_position = 10

    # Modified list of attributes to maintain consistent line spacing
    attributes = [
        ("i_am", profile.i_am),
        ("use", profile.use),
        ("cloud", profile.cloud),
        ("specialize", profile.specialize),
        ("edu", profile.edu)
    ]

    for name, value in attributes:
        if isinstance(value, list):
            draw.text((10, y_position), f"{name}=" + repr(value) + ",", font=font, fill='white')
        else:
            draw.text((10, y_position), value, font=font, fill='white')
        y_position += 30

    # Save the banner
    banner.save("my_banner.png")

if __name__ == "__main__":
    Profile = namedtuple('Profile', ['i_am', 'use', 'cloud', 'specialize', 'edu'])
    user_profile = Profile(
        i_am=["software engineer", "tech enthusiast", "make cloud stuff connect", "like to get my hands dirty"],
        use=["Kubernetes", "Go/Python/C++", "Linux", "Docker", "DevOps"],
        cloud=["AWS", "GCP", "Azure"],
        specialize=["Automation", "Micro-services", "REST-API"],
        edu=["B.Sc Mathematics and computer science", "M.Sc Computer Science - ONGOING"]
    )
    create_banner_with_transparent_bg("bg.png", user_profile)
