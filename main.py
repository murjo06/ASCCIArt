from PIL import Image
import imageProcessor
import asciiConverter
import consoleAnimator
import os

image = Image.open("meme.gif")
frames = imageProcessor.getFrames(image)

width = 128

i = 0
allFrames = []
for frame in frames:
    art = asciiConverter.convertToAsciiArt(frame, width)
    asciiConverter.saveAsText(art, "frames" + os.sep + f"{i}.txt")
    allFrames.append(art)
    i += 1
consoleAnimator.draw(allFrames, 0.1)