from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    starting_color = image[sr][sc]
    r,c = len(image), len(image[0])
    DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(sr, sc)]
    v = set()
    
    while q:
        cur = q.pop()
        v.add(cur)
        
        for d in DIR: # Append neighbours
            n = (cur[0] + d[0], cur[1] + d[1])
            if n[0] < 0 or n[0] >= r or n[1] < 0 or n[1] >= c or image[n[0]][n[1]] != starting_color or n in v:
                continue
            else:
                q.append(n)
        
        image[cur[0]][cur[1]] = color # Change color
    
    return image

a = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(a)