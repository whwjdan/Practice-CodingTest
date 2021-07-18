def chk(i, j):
    global b
    global arr_chk
    block = b[i][j]
    if b[i+1][j] == block and b[i][j+1] == block and b[i+1][j+1] == block and block !=0:
        arr_chk[i][j], arr_chk[i+1][j], arr_chk[i][j+1], arr_chk[i+1][j+1] = 1, 1, 1, 1
    return 0

def down_block(h,w):
    global b
    for i in range(w):
        c = []
        for j in range(h-1, -1, -1):
            if b[j][i] != 0:
                c.append(b[j][i])
        for j in range(h-1, -1, -1):
            if len(c) != 0:
                b[j][i] = c.pop(0)
            else:
                b[j][i] = 0
                
def solution(m, n, board):
    global arr_chk
    global cnt
    global b
    b = []
    for i in range(len(board)):
        b.append(list(board[i]))

    cnt = 0
    arr_chk = [[0 for i in range(n)] for j in range(m)]
    print(m,n)

    #m, n : 세로 가로
    # 왼쪽위 기준으로 자신, 우, 하, 대각아래 체크, 세로 1~m까지 가로 0~n-1까지
    
    h, w = len(board), len(board[0])
    
    
    while True:
        for i in range(0, h-1):
            for j in range(0, w-1):
                chk(i, j)

        val = 0
        for i in range(h):
            for j in range(w):
                val += arr_chk[i][j]
        
        if val == 0:
            break
    # cnt증가 후 배열 초기화
        for i in range(h):
            for j in range(w):
                if arr_chk[i][j] == 1:
                    b[i][j] = 0
                    cnt += 1
            
        down_block(h,w)
        
        arr_chk = [[0 for i in range(n)] for j in range(m)]

    return cnt

#feat(Jeongmu-Jo): [카카오, 2018블라인드] 프렌즈4블럭