import cv2
import time
from queue import PriorityQueue
from itertools import count

class Point:
    def __init__(self, m_y, m_x):
        self.y = m_y
        self.x = m_x

    def __hash__(self):
        return hash((self.y, self.x))

    def __eq__(self, another):
        return (self.y, self.x) == (another.y, another.x)


# Heuristic 1: 3D Manhattan

def heuristic1(map, a: Point, b: Point):   
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dz = abs(delta_a(map, a, b))
    return (dx + dy + dz)
 

# Heuristic 2: 3D Euclidean

def heuristic2(map, a: Point, b:Point):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dz = abs(delta_a(map, a, b))
    return (dx * dx + dy * dy + dz * dz)**(1/2)


# Heuristic 3: 3D Squared-Euclidean

def heuristic3(map, a: Point, b: Point):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dz = abs(delta_a(map, a, b))
    return (dx * dx + dy * dy + dz * dz)


# Heuristic 4: 3D Diagonal (Octile)

def heuristic4(map, a: Point, b: Point):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dz = abs(delta_a(map, a, b))
    return max(dx,dy,dz) + (2**(1/2) - 1) * min(dx,dy,dz)
    

# get available points around the current

def getNeighbors(map, point: Point):
    neighbors = []
    i, j = point.y, point.x
    r, c = map.shape[0], map.shape[1]

    if i > 0:                       neighbors.append(Point(i - 1, j))
    if j > 0:                       neighbors.append(Point(i, j - 1))
    if i < r - 1:                   neighbors.append(Point(i + 1, j))
    if j < c - 1:                   neighbors.append(Point(i, j + 1))
    if i > 0 and j > 0:             neighbors.append(Point(i - 1, j - 1))
    if i > 0 and j < c - 1:         neighbors.append(Point(i - 1, j + 1))
    if i < r - 1 and j > 0:         neighbors.append(Point(i + 1, j - 1))
    if i < r - 1 and j < c - 1:     neighbors.append(Point(i + 1, j + 1))

    return neighbors


# sign of a

def sgn(a):
    if a == 0:
        return 0
    return a/abs(a)


# get distance between a and b

def d(map, height, a: Point, b: Point):
    return ((a.y-b.y)**2+(a.x-b.x)**2)**(1/2) + (sgn(height)/2+1)*abs(height)


# get height between a and b

def delta_a(map, a: Point, b: Point):
    return int(map[a.y][a.x]) - int(map[b.y][b.x])


# visualize

def visualizePath(map, path, current, heuristicID: int):

    # reopen as RGB map
    map = cv2.cvtColor(map, cv2.COLOR_GRAY2RGB)

    while current in path:

        # get the coordinate
        map[current.y][current.x] = (0, 255, 255)
        
        # bold
        neighbors = getNeighbors(map, current)
        for neighbor in neighbors:
            map[neighbor.y][neighbor.x] = (0, 255, 255)

        current = path[current]

    # save
    status = cv2.imwrite(f'./map{heuristicID}.bmp', map)

    return status


def A_Star_Algorithm(map, start: Point, end: Point, m: int, heuristic, heuristicName: str, heuristicID: int):
    
    print(f"\nHeuristic{heuristicID}: Finding path using {heuristicName}...")

    # starting algorithm time
    startTime = time.time()
    
    # to calc the number of interacted points
    interactedPoints = set()

    unique = count()
    cols, rows = map.shape

    openSet = PriorityQueue()
    openSet.put((0, next(unique), start))

    gScores = [[1000000]*rows for i in range(cols)]
    gScores[start.y][start.x] = 0

    # to keep track of the path using Dictionary
    path = {}

    while not openSet.empty():

        # Lowest Cost node / winner / current is the next one to be picked
        current = openSet.get()[2]

        # if it is destination, got it
        if current == end:

            totalTime = time.time() - startTime
            print("DONE!")
            
            # draw path & save picture
            if (visualizePath(map, path, end, heuristicID)):
                print(f"Saved map{heuristicID} successfully!")
            else:
                print(f"Cannot save map{heuristicID}.")

            # write to output[i].txt
            file = open(f"./output{heuristicID}.txt", 'w')
            file.write(f"{gScores[end.y][end.x]}\n{len(interactedPoints)}")
            print(f"Wrote to output{heuristicID}.txt successfully!")
            file.close()
            
            print(f"Runtime: {totalTime} second(s)")
            
            return True

        nbs = getNeighbors(map, current)
        interactedPoints.update(nbs)

        for neighbor in nbs:

            if abs(delta_a(map, neighbor, current)) > m:
                continue

            height = delta_a(map, current, neighbor)

            # tentative gScore
            newgScore = gScores[current.y][current.x] + d(map, height, current, neighbor)

            if newgScore < gScores[neighbor.y][neighbor.x]:
                path[neighbor] = current
                gScores[neighbor.y][neighbor.x] = newgScore
                f = newgScore + heuristic(map, neighbor, end)
                openSet.put((f, next(unique), neighbor))

    totalTime = time.time() - startTime    
    print("ERROR: Cannot find path!")
    print(f"Runtime: {totalTime} second(s)")
    
    return False
