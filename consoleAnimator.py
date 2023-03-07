import time
import os

def draw(output: list, delay):
    k = 0
    prints = []
    for i in output:
        lines = ""
        for j in i:
            lines += j
            lines += os.linesep
        prints.append(lines)
    while True:
        print(prints[k % len(prints)], sep="", end="", flush=True)
        time.sleep(delay)
        print("\033[H\033[3J")
        k += 1