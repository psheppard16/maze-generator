import sys
import json
import gridSquare
# args = sys.argv
# if len(args) != 3:
#     Exception("you must provide three arguments: width, length, and wall size")
# else:
#     width = int(args[1])
#     length = int(args[2])
#     wallSize = int(args[3])
#     walls = mazeGenerator.generateSquareMaze(width, length, wallSize)
#     with open('maze.json', 'w') as outfile:
#         json.dump(walls, outfile)
width = 10
length = 10
wallSize = 100
walls = gridSquare.generateSquareMaze(width, length, wallSize)
with open('maze.json', 'w') as outfile:
    json.dump(walls, outfile)