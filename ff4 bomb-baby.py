
def solution(x, y):
    big, smol = max(int(x),int(y)) , min(int(x),int(y))
    mod=1
    cnt = 0
    while mod!=0:
        if(smol == 1):
            return str(cnt + big//smol -1 )
        mod = big%smol
        cnt += big//smol
        big = max(mod,smol)
        smol = min(mod,smol)
        
    return "impossible"
print(solution('22', '7'))
