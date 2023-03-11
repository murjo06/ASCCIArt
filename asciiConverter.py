from PIL import Image

asciiCharactersBySurface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def convertToAsciiArt(image: Image):
    art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ""
        for x in range(0, width - 1):
            coordinate = x, y
            pixel = image.getpixel(coordinate)
            line += convertPixelToCharacter(pixel)
        art.append(line)
    return art

def convertPixelToCharacter(pixel):
    (r, g, b) = pixel
    pixelBrightness = r + g + b
    maxBrightness = 255 * 3
    brightnessWeight = len(asciiCharactersBySurface) / maxBrightness
    index = int(pixelBrightness * brightnessWeight) - 1
    return asciiCharactersBySurface[index]

def saveAsText(art: str, location: str):
    with open(location, "w") as file:
        for line in art:
            file.write(line)
            file.write("\n")
        file.close()