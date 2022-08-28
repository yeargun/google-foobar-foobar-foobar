

# def solution(width,height,state):
#     total = 1
#     for i in range(1,width*height+1):
        
#         print(i,
#             (m.factorial(i+height-1)/( m.factorial(i-1) * m.factorial(i)))
#             *
#             (m.factorial(i+width-1)/( m.factorial(i-1) * m.factorial(i)))
#             *
#             (state-1)**i
#         )

#     return total


# it actualy is 
# for i in range n, where n is width*height
#      count +=
#      (number of possible sum combinations of numbers thats add up to i, number count is max width
#      times
#      number of possible sum combinations of numbers thats add up to i, number count is max height
#      times
#      numberOfStates^i)
# got solution from :
# https://github.com/franklinvp/foobar/blob/master/foobar2020/solutionProblem1.py
# number-of-possible-combinations-of-x-numbers-that-sum-to-y:
# https://math.stackexchange.com/questions/1462099/number-of-possible-combinations-of-x-numbers-that-sum-to-y

from collections import Counter

def buildGCDTable(n):
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == 0 or j == 0:
                result[i][j] = 1
                result[j][i] = 1
            elif i == j:
                result[i][j] = i+1
            else:
                result[i][j] = result[i][j-i-1]
                result[j][i] = result[i][j-i-1]
    return result

def gcd(x,y, gcdTable):
    return gcdTable[x-1][y-1]

def buildFactorialTable(n):
    result = [1]
    for i in range(n-1):
        result.append(result[-1]*(i+2))
    return result

def factorial(x, factorialTable):
    return factorialTable[x-1]

def coefficientFactor(c, n,factorialTable):

    cc=factorial(n,factorialTable)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b,factorialTable)
    return cc

def partitionsAndCycleCount(n, factorialTable):
    k = 0  # Index of last element in a partition 
    p = n*[0] # To store a partition in p[0:k+1]
    p[0] = n  # First partition is [n]
    result = [] # To store all partitions
    # The loop stops when the current partition has all 1s 
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    result = []
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partition = a[:k+2]
            result.append((partition, coefficientFactor(partition,n,factorialTable)))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partition = a[:k+1]
        result.append((partition, coefficientFactor(partition,n,factorialTable)))
    return result

def solution(w, h, s):

    n = max(w,h)
    gcdTable = buildGCDTable(n)

    factorialTable = buildFactorialTable(n)
    
    grid=0
    for cpw in partitionsAndCycleCount(w,factorialTable):
        for cph in partitionsAndCycleCount(h,factorialTable):
            m=cpw[1]*cph[1]
            grid+=m*(s**sum([sum([gcd(i, j, gcdTable) for i in cpw[0]]) for j in cph[0]]))
    return str(grid//(factorial(w,factorialTable)*factorial(h,factorialTable)))

print(solution(2,3,4))

