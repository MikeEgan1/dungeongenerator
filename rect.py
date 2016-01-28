import sys


class Rect:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, xcorner, ycorner, width, height):
        self.x1 = xcorner
        self.y1 = ycorner
        self.x2 = xcorner + width
        self.y2 = ycorner + height
        self.height = height
        self.width = width

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)


    def print_rect(self):
        for _ in xrange(self.x2 - self.x1):
            for _ in xrange(self.y2 - self.y1):
                sys.stdout.write('X')
            sys.stdout.write('\n')