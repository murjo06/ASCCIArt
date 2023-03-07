from PIL import Image
import imageProcessor
import time

image = Image.open("cow.gif")
frames = imageProcessor.getFrames(image)

animation = "|/-\\"
idx = 0
while True:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)