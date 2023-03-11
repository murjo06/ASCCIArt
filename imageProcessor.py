from PIL import Image
import numpy

def getFrames(source: Image):
    frames = []
    for frame in range(0, getattr(source, "n_frames", 1)):
        source.seek(frame)
        img = source.copy()
        frames.append(img)
    return frames