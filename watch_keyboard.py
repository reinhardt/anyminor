# -*- coding: utf-8 -*-
from time import sleep
from time import time
import keyboard
import sys

mean_interval = 60.0

if __name__ == "__main__":
    queue, _ = keyboard.start_recording()
    batch = []
    speed = 0.0
    while True:
        sleep(0.05)
        while not queue.empty():
            current = queue.get()
            batch.append(current)
            queue.task_done()
        batch = [item for item in batch if time() - item.time < mean_interval]
        speed = len(batch) / mean_interval
        sys.stdout.write("{}\n".format(speed))
        sys.stdout.flush()
