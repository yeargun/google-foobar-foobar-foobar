# MAX_BUNNY_SIZE = 2000000
# def solution(entrances, exits, path):
#     headCount = [0] * len(path)
#     #spaceLeft at each room
#     spacesLeft = []
#     for i in range(len(path)):
#         room = path[i]
#         if i in entrances:
#             headCount[i] = MAX_BUNNY_SIZE
#         # elif i in exits
#     for room in path:
#         sumNext = 0
#         for next in room:
#             sumNext+=next
#         spacesLeft.append(sumNext)
    
#     for exitNums in exits:
#         spacesLeft[exitNums] = MAX_BUNNY_SIZE

#     # print("Left spaces: ",leftSpaces)
#     # print("HeadCount:", headCount )
#     # print("@@@@Init the passenger entrances@@@@")
#     for entrance in entrances:
#         for toPath in range(len(path[entrance])):
#             traverseSome(entrance, toPath, path[entrance][toPath], spacesLeft, headCount)
#     # print("Left spaces: ",leftSpaces)
#     # print("HeadCount:", headCount )


#     totalLeft = 0
#     for roomNum in range(len(path)):
        
#         if roomNum in entrances: continue
#         if roomNum in exits:
#             totalLeft += headCount[roomNum]
#         for toPath in range(len(path[roomNum])):
#             traverseSome(roomNum, toPath, path[roomNum][toPath], spacesLeft, headCount)
#     # print(totalLeft)
#     return totalLeft





def traverseSome(room0, room1, bunnyAmount, leftSpaces, headCount):
    if(leftSpaces[room1]>0):
        bunnyAmount = headCount[room0] if headCount[room0] < bunnyAmount else bunnyAmount
        passengerCount = bunnyAmount if leftSpaces[room1]>bunnyAmount else leftSpaces[room1]
        headCount[room0] -=passengerCount
        headCount[room1] +=passengerCount
        leftSpaces[room1] -=passengerCount
    else:
        return




## fill from entrances
## count current population of rooms
## while mid rooms contain bunny, try




def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    print(visited)
    queue = [source]
    while len(queue) > 0:
        top = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[top][i][1] - matrix[top][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    # Get route
                    visited[destination] = top
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    # Get flow value and update augmented graph
                    temp = 1
                    total = float("inf")
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        cur = path[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        if entry[1] < 0: # Already augmented need to flip
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][cur]
                        if entry[1] <= 0: # Already augmented need to flip
                            entry[1] -= total
                        else:
                            entry[0] += total
                        cur = path[temp]
                        temp += 1
                    print("true")
                    
                    return True
                else:
                    visited[i] = top
                    queue.append(i)
    return False

def solution(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    aug = []
    for i in range(len(path)):
        aug.append([])
        for j in range(len(path[i])):
            aug[i].append([0, path[i][j]])
        aug[i].append([0, 0])
        if i in exits:
            aug[i].append([0, max_val])
        else:
            aug[i].append([0, 0])
    aug.append([])
    aug.append([])
    print(np.matrix(aug))
    for i in range(len(path[0]) + 2):
        if i in entrances:
            aug[-2].append([0, max_val])
        else:
            aug[-2].append([0, 0])
        aug[-1].append([0, 0])
    print(aug)
    while bfs(aug, len(aug)-2, len(aug)-1):
        pass
    total = 0
    for i in range(len(aug)):
        total += aug[-2][i][0]
    print(total)
    return total



solution([0, 1], [4, 5],
[[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])