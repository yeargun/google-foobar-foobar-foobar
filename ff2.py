# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, 
# and y being the height from the ground. 

# For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, 
# and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely 
# (Commander Lambda has been adding a LOT of workers). 


def solution(x,y):
    # answer = 1
    # for i in range(x):
    #     answer += i
    # for j in range(x+1,x+y):
    #     answer += j

    # 1 + 2 + .. x-1 +  x+1 + x+2 + ... + x+y-1
    # ((x+y) * (x+y-1))/ 2  - x 
    return str((x+y)*(x+y-1) // 2 - y+1)