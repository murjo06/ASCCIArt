import numpy as numpy
import cv2

def format_timedelta(timedelta):
    result = str(timedelta)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frames_durations(video, saving_fps):
    s = []
    clip_duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
    for i in numpy.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def get_frames(video, FPS):
    frames = []
    video_fps = video.get(cv2.CAP_PROP_FPS)
    saving_frames_per_second = min(video_fps, FPS)
    saving_frames_durations = get_saving_frames_durations(video, saving_frames_per_second)
    count = 0
    while True:
        is_read, frame = video.read()
        if not is_read:
            break
        frame_duration = count / video_fps
        try:
            closest_duration = saving_frames_durations[0]
        except IndexError:
            break
        if frame_duration >= closest_duration:
            frames.append(frame)
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        count += 1
    return frames