import re
from Algorithms import *

def main():

    map = cv2.imread('map.bmp', 0)

    input = open('input.txt', 'r')

    st = tuple([int(s) for s in re.findall(r'\d+', input.readline())])
    ed = tuple([int(s) for s in re.findall(r'\d+', input.readline())])
    m = int(input.readline())

    input.close()
    
    print(st, ed, m)

    heuristicList = [heuristic1, heuristic2, heuristic3, heuristic4]
    heuristicName = ["Manhattan Distance",
                     "Euclidean Distance",
                     "Euclidean-Squared Distance",
                     "Diagonal Distance (Octile)"]
    
    for i in range(len(heuristicList)):
        A_Star_Algorithm(map, Point(st[1], st[0]), Point(ed[1], ed[0]), m, heuristicList[i], heuristicName[i], i + 1)
    
if __name__ == "__main__":
    main()
