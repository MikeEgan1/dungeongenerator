import sys


class Rect:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, xcorner, ycorner, width, height):
        self.x1 = xcorner
        self.y1 = ycorner
        self.x2 = xcorner + width
        self.y2 = ycorner + height

    def print_rect(self):
        for x in xrange(self.x2 - self.x1):
            for y in xrange(self.y2 - self.y1):
                sys.stdout.write('X')
            sys.stdout.write('\n')
