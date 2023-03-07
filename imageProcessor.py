from PIL import Image

def getFrames(source: Image):
    frames = []
    for frame in range(0, source.n_frames):
        source.seek(frame)
        img = source.copy().convert("RGB")
        frames.append(img)
    return frames