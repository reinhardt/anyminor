# -*- coding: utf-8 -*-
from simpleaudio import WaveObject
import sys

loops = {
    4.5: WaveObject.from_wave_file("4_Loop.wav"),
    3.0: WaveObject.from_wave_file("3_Loop.wav"),
    1.5: WaveObject.from_wave_file("2_Loop.wav"),
    0.0: WaveObject.from_wave_file("1_Loop.wav"),
}


def get_loop(speed):
    for key in loops.keys():
        if speed >= key:
            return loops[key]


if __name__ == "__main__":
    speed = 0.0
    current_loop = None
    line = sys.stdin.readline().strip()
    while True:
        if not current_loop or not current_loop.is_playing():
            current_loop = get_loop(speed).play()
        line = sys.stdin.readline().strip()
        if line:
            speed = float(line)
