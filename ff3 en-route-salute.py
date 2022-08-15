#en-route-salute

#righter count = # of lefters on right side
#left count = # of righters on left side
# can we access stuff in o(1)



def solution(s):
    currRighterCount = 0
    handshake = 0
    for i in range(len(s)):
        if(s[i]=="<"):
            handshake+=currRighterCount
        elif(s[i]==">"):
            currRighterCount+=1
    
    return handshake*2



print(solution("<<>><"))