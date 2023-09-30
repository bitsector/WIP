#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont

def create_banner(bg_color, text):
    # Create a plain grey background with double the LinkedIn recommended resolution
    banner = Image.new('RGB', (3168, 792), bg_color)
    
    # Draw text on the banner
    draw = ImageDraw.Draw(banner)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to DejaVuSans-Bold font on Ubuntu
    font_size = 50
    font = ImageFont.truetype(font_path, font_size)
    
    y_position = 20  # Starting from the top
    x_position = 20  # Start from the upper left

    # Split the text by lines and draw each line
    for line in text.splitlines():
        draw.text((x_position, y_position), line, font=font, fill='white')
        y_position += 60  # Adjust spacing between lines

    # Resize the image to fit LinkedIn's recommended size
    banner = banner.resize((1584, 396))

    # Save the banner
    banner.save("my_banner.png")

if __name__ == "__main__":
    with open("desired_text.txt", "r") as file:
        text = file.read()
    create_banner("#B0B0B0", text)  # #B0B0B0 is a shade of grey similar to the background of the provided image
