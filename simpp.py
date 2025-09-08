#!/usr/bin/python3

# test2
from time import sleep

FPS=8
BUFFER=100*'\n'
ANIMS = ["walk", "wave", "kupers"]
ANCHORCHARS = ('*','^','A') # (fillerchar, anchor, new anchor)
ANIMDIR = "./animations"

class Animation():
    def __init__(self, filename, name=""):
        if name:
            self.name = name
        else:
            self.name = filename

        self.frames = []
        NewFrame = Frame()
        with open(f"{ANIMDIR}/{filename}.txt", 'r') as f:
            for line in f.readlines():
                if line.startswith(ANCHORCHARS):
                    a1 = line.find(ANCHORCHARS[1])
                    a2 = line.find(ANCHORCHARS[2])
                    NewFrame.anchor1 = a1
                    NewFrame.anchor2 = a2 if ( a2 >= 0 ) else a1
                    # check last char for frame count
                    n = line.strip()[-1]
                    if n.isnumeric():
                        NewFrame.fps /= int(n)

                    self.frames.append(NewFrame)
                    NewFrame = Frame()
                else:
                    NewFrame.content += line

class Frame(Animation):
    def __init__(self):
        self.anchor1 = 0
        self.anchor2 = 0
        self.content = ""
        self.fps = FPS

class Dude():
    def __init__(self):
        self.x = 0
        self._walk = Animation("walk")
        self._wave = Animation("wave")
        self._kupers = Animation("kupers")

    def walk(self, n=5):
        self.play(self._walk, n)

    def wave(self, n=5):
        self.play(self._wave, n)

    def kupers(self, n=1):
        self.play(self._kupers, n)

    def play(self, animation, n):
        a = self.x
        frames = animation.frames
        for loops in range(n):
            for frame in frames:
                print(BUFFER)
                a1 = a - frame.anchor1
                x = a1*' '
                for line in frame.content.splitlines():
                    print(f"{x}{line}")

                a = a1 + frame.anchor2
                sleep(1/frame.fps)

        self.x = a


if __name__ == "__main__":
    dude = Dude()
    dude.walk()
    dude.wave()
    dude.kupers()

