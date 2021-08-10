from itertools import combinations

def solution(relation):
    answer = 0
    reverse = list(zip(*relation))
    
    #print(reverse)
    
    row = len(reverse[0])
    col = len(reverse)
    print(col, row)
    
    temp = []
    
    for c in range(col):
        if len(reverse[c]) == len(set(reverse[c])):
            answer += 1
        else:
            temp.append(reverse[c])
    
    print(temp)
    
    idx = [i for i in range(len(temp))]
    print('----------------------------')
    for k in range(2, len(temp) + 1):
        for li in combinations(idx, k):
            print(li)
            res = list(temp[i] for i in li)
            res = list(zip(*res))
            print('res', res)
            
    
    return answer
