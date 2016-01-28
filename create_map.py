from rect import Rect
from tile import Tile
import sys
import random

MAP_HEIGHT = 50
MAP_WIDTH = 50
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 5`


def create_room(room, dungeon_map):
    for x in xrange(room.x1 + 1, room.x2):
        for y in xrange(room.y1 + 1, room.y2):
            dungeon_map[x][y] = 'X'
    return dungeon_map

def print_dungeon_map(dungeon_map):
    for x in xrange(MAP_WIDTH):
        for y in xrange(MAP_HEIGHT):
            sys.stdout.write(dungeon_map[x][y])
        sys.stdout.write('\n')

def main():
    dungeon_map = [['_' for x in xrange(MAP_HEIGHT)] for x in xrange(MAP_WIDTH)]
    rooms = []
    num_rooms = 0

    for r in xrange(MAX_ROOMS):
        width = random.randrange(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        height = random.randrange(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        xcorner = random.randrange(0, MAP_WIDTH - width - 1)
        ycorner = random.randrange(0, MAP_HEIGHT - height - 1)
        new_room = Rect(xcorner, ycorner, width, height)
        # new_room.print_rect()

        if num_rooms > 1:
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break

                create_room(new_room, dungeon_map)
                rooms.append(new_room)
                print getattr(new_room, 'width')
                print getattr(new_room, 'height')
        else:
            create_room(new_room, dungeon_map)
            rooms.append(new_room)
            print getattr(new_room, 'width')
            print getattr(new_room, 'height')

    print_dungeon_map(dungeon_map)

if __name__ == "__main__":
    main()