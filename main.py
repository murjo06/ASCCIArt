from PIL import Image
import imageProcessor
import asciiConverter
import consoleAnimator
import videoProcessor
import cv2

FRAMES_PER_SECOND = 5
WIDTH = 128

imagePath = "sus.jpg"
videoPath = "chad.mp4"

def drawVideo(video_path: str):
    video = cv2.VideoCapture(video_path)
    frames = videoProcessor.get_frames(video, FRAMES_PER_SECOND)
    images = []
    for frame in frames:
        image = Image.fromarray(frame).convert("RGB")
        image = image.resize((WIDTH, round(0.5 * WIDTH / (image.width / image.height))), Image.NEAREST)
        art = asciiConverter.convertToAsciiArt(image)
        images.append(art)
    consoleAnimator.drawVideo(images, 1 / FRAMES_PER_SECOND)

def drawImage(image_path: str):
    image = Image.open(image_path)
    if getattr(image, "is_animated", False):
        frames = imageProcessor.getFrames(image)
        i = 0
        allFrames = []
        for frame in frames:
            art = asciiConverter.convertToAsciiArt(frame.resize((WIDTH, round(0.5 * WIDTH / (frame.width / frame.height))), Image.NEAREST).convert("RGB"))
            allFrames.append(art)
            i += 1
        consoleAnimator.drawVideo(allFrames, 0.1)
    else:
        art = asciiConverter.convertToAsciiArt(image.resize((WIDTH, round(0.5 * WIDTH / (image.width / image.height))), Image.NEAREST).convert("RGB"))
        consoleAnimator.draw(art)

drawImage(imagePath)