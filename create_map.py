from rect import Rect
from tile import Tile
import sys
import random

MAP_HEIGHT = 50
MAP_WIDTH = 50
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 5


def create_room(room, dungeon_map):
    for x in xrange(room.x1 + 1, room.x2):
        for y in xrange(room.y1 + 1, room.y2):
            dungeon_map[x][y] = 'X'
    return dungeon_map

def create_h_tunnel(x1, x2, y, dungeon_map):
    #horizontal tunnel. min() and max() are used in case x1>x2
    for x in xrange(min(x1, x2), max(x1, x2) + 1):
        dungeon_map[x][y] = 'X'
    return dungeon_map

def create_v_tunnel(y1, y2, x, dungeon_map):
    #vertical tunnel
    for y in xrange(min(y1, y2), max(y1, y2) + 1):
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
                (new_x, new_y) = new_room.center()
                (prev_x, prev_y) = rooms[num_rooms-1].center()

                if random.randrange(0, 1) == 1:
                    #first move horizontally, then vertically
                    dungeon_map = create_h_tunnel(prev_x, new_x, prev_y, dungeon_map)
                    dungeon_map = create_v_tunnel(prev_y, new_y, new_x, dungeon_map)
                else:
                    #first move vertically, then horizontally
                    dungeon_map = create_v_tunnel(prev_y, new_y, prev_x, dungeon_map)
                    dungeon_map = create_h_tunnel(prev_x, new_x, new_y, dungeon_map)

                num_rooms = num_rooms + 1

        else:
            create_room(new_room, dungeon_map)
            rooms.append(new_room)
            num_rooms = num_rooms + 1

    print_dungeon_map(dungeon_map)

if __name__ == "__main__":
    main()