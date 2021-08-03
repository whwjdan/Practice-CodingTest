Board = []

def canFill(row, col):
    # 위에서 아래로 내려가면서 0 ~ 해당 행렬 좌표로 가면서
    # 3 *2 or 2 * 3중 현재 0이지만 채워야하는 경우 위에서부터 0인지 체크해서
    # 모두 0이면 채울 수 있기 때문에 True return
    for i in range(row):
        if Board[i][col]:
            return False
    return True

def find(row, col, h, w):
    emptyCnt = 0
    # lastValue -> 3*2 or 2*3영역에서 숫자가 같은 숫자인지 체크하기 위해 사용
    lastValue = -1
    # 3*2 or 2*3 행렬에서 빈칸 0에 숫자를 채워야하므로 0일때 검은블록을 채울수있는지 체크
    
    for r in range(row, row + h):
        for c in range(col, col + w):
            if Board[r][c] == 0:
                if canFill(r, c) == False:
                    return False
                emptyCnt += 1
                if emptyCnt > 2:
                    return False
            else:
                # lastValue -> -1인 경우는 초기값
                if lastValue == -1:
                    lastValue = Board[r][c]
                # 초기값이 아닌데 값이 다른경우 ex) 2*3영역에서 1과 2가 섞여있을때
                elif lastValue != Board[r][c]:
                    return False
    # 위의 모든 조건을 통과한 경우 : 지울 수 있는 경우 0으로 지워준다.
    for r in range(row, row + h):
        for c in range(col, col + w):
            Board[r][c] = 0
    return True
                    

def solution(board):
    global Board
    Board = board
    n = len(board)
    answer = 0
    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                # 가로로 블록 삭제가 가능한지 확인
                # find(row, col, h, w)이고 row의 범위가 row + r
                # col의 범위가 col+w이므로 10*10 행렬일때 i는 8, j는 7까지 가능하다
                if i <= n-2 and j <= n-3 and find(i,j,2,3):
                    cnt += 1
                elif i <= n-3 and j <= n-2 and find(i,j,3,2):
                    cnt += 1
        answer += cnt
        if cnt == 0:
            break
    return answer

    

def chk_rec(board, num):
    # 위에서 아래로 내려오면서 한 세로줄 마다 스택으로 넣고 첫행의 num의 개수를 cnt로 정하고
    # 그 다음 행에서 cnt와 개수가 똑같은지 확인
    ck, ck_two = False, False
    chk_cnt, cnt = 0, 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == num:
                chk_cnt += 1
                ck = True
        if ck:
            idx = i
            break
    if chk_cnt < 2:
        print('chk_cnt < 2')
        return False
    
    if ck and idx + 1 < len(board):
        for i in range(idx + 1, len(board)-1, 1):
            cnt = 0
            exist_num = False
            for j in range(len(board)):
                if board[j][i] == num:
                    cnt += 1
                    exist_num = True
            if cnt != chk_cnt and exist_num:
                return False
    return True
#feat(Jeongmu-Jo): [카카오, 2019블라인드] 블록게임
