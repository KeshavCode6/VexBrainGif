from PIL import Image
import sys

# Number of key frames to extract
num_key_frames = int(sys.argv[2])

# Open the GIF image
with Image.open('bad.gif') as im:
    # Loop to extract and save key frames
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save(f'{i}.png')

# Function to convert RGB to HEX
def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Process each saved frame
def run(i):
    try:
        # Load the image
        image = Image.open(f"{i}.png")
    except IOError:
        print("Unable to load image")
        raise

    # Convert image to RGB if it's not already in this mode
    image = image.convert('RGB')

    # Get image size
    width, height = image.size

    # Extract pixel data
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            row.append(rgb2hex(pixel[0], pixel[1], pixel[2]))
        pixels.append(row)
    
    # Print pixel data (this will print a lot of data; consider saving to a file or handling differently if needed)
    print(pixels)

run(sys.argv[1])
