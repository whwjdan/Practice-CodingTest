Board = []

                    

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

    
# 초기에 풀려고 만들었던 함수
# 검은블록을 채운뒤 이중포문을 돌면서 해당 숫자가 직사각형인지 체크하는 함수를 만들었었다.
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
