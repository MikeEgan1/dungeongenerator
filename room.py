from rect import Rect
from tile import Tile

MAP_HEIGHT = 200
MAP_WIDTH = 200

def create_room(room):
    global map
    #go through the tiles in the rectangle and make them passable
    for x in xrange(room.x1, room.x2 + 1):
        for y in xrange(room.y1, room.y2 + 1):
            map[x][y].blocked = False
            map[x][y].block_sight = False

def create_h_tunnel(x1, x2, y):
    global map
    for x in xrange(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
    global map
    #vertical tunnel
    for y in xrange(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def make_map():
    global map

    #fill map with "blocked" tiles
    map = [[ Tile(True)
             for y in xrange(MAP_HEIGHT) ]
           for x in xrange(MAP_WIDTH) ]

    #create two rooms
    room1 = Rect(20, 15, 10, 15)
    room2 = Rect(50, 15, 10, 15)
    create_h_tunnel(25, 55, 23)
    create_room(room1)
    create_room(room2)