from PIL import Image

def getFrames(source: Image):
    frames = []
    for frame in range(source.n_frames):
        source.seek(source.n_frames // source.n_frames * frame)
        frames.append(source)
    return frames