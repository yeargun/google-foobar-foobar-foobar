# def solution(n):
# # max 19bricks, so
# # 19bricks left to right, 
# # right bigger than left or right is 0 or i is 18
# # left to right sum = n


#     for i in range(19):
#         None
#     return 





# its given solution(200) is 487067745
# In Exponential Form:
# 3^1 x 5^1 x 107^1 x 303469^1
# hmm

#something recursive maybe



def solution(n):
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    print(len(m[0]))
    m[0][0] = 1  # base case
    for stair in range(1, n + 1):
        for left in range(0, n + 1):
            m[stair][left] = m[stair - 1][left]
            if(left >= stair):
                m[stair][left] += m[stair - 1][left - stair]
	          	
    return m[n][n] -1


print(solution(20))