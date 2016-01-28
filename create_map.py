from rect import Rect
from tile import Tile
import random

MAP_HEIGHT = 50
MAP_WIDTH = 50
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 3

def main():
    dungeon_map = [['_']*MAP_WIDTH]*MAP_HEIGHT
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

                rooms.append(new_room)
        else:
            rooms.append(new_room)

    for room in rooms:
        room.print_rect()



if __name__ == "__main__":
    main()