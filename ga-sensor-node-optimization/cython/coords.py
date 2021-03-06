coords = [(0,0), (7,6), (6,16),
           (19,16), (10,8), (18,2),
           (10,10),
              (4,15),
              (4,19),
              (20,4),
              (5,17),
              (15,15),
              (13,9),
              (19,1),
              (5,7),
              (5,19),
              (4,20),
              (10,16),
              (5,2),
              (18,17),
              (13,10),
              (1,18),
              (16,4),
              (16,16),
              (16,18),
              (9,20),
              (6,16),
              (4,6),
              (3,18),
              (12,10),
              (17,17),
              (0,18),
              (18,15),
              (10,8),
              (5,4),
              (17,18),
              (19,16),
              (5,17),
              (7,8),
              (7,3),
              (8,18),
              (11,14),
              (5,17),
              (15,8),
              (15,4),
              (19,15),
              (4,5),
              (2,4),
              (5,18),
              (11,9)]
import random
from conf import NUM_NODES
#NUM_NODES = 100
FIELD_HEIGHT = 20
FIELD_WIDTH = 20

possible_coords = [ (x,y) for x in range(FIELD_WIDTH+1) for y in range(FIELD_HEIGHT+1) ]
coords = []
for i in range(NUM_NODES):
    coords.append(random.choice(possible_coords))
    possible_coords.remove(coords[i])
