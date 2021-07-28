def convert(k, n):
    T = "0123456789ABCDEF"
    i,j = divmod(k, n)
    if i == 0:
        return T[j]
    else:
        return convert(i, n) + T[j]

def solution(n,t,m,p):
    i = 0
    nums = []
    while len(nums) < t*m:
        nums += list(convert(i,n))
        i += 1
    result = nums[p-1:t*m:m]
    result = ''.join(result)
    return result
    
#feat(Jeongmu-Jo): [카카오, 2018블라인드] n진수 게임
