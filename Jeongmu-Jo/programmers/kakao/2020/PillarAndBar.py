Pillar = [[]]
Bar = [[]]

def checkPillar(x, y):
    # 바닥이 0 or 아래가 기둥 or 보가 한쪽 끝에 있을 때
    if y == 0 or Pillar[x][y-1]:
        return True
    # 보의 한쪽 끝부분에 있을 때
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]:
        return True
    return False

def checkBar(x, y):
    # 한쪽 끝이 기둥위에 있을 때
    if Pillar[x][y-1] or Pillar[x+1][y-1]:
        return True
    # 양쪽 끝이 다른 보와 동시에 연결되어 있을때
    if x > 0 and Bar[x-1][y] and Bar[x+1][y]:
        return True
    return False

def canDelete(x, y):
    # 아래를 제외한 좌, 우, 상좌, 상우, 상, 자신의 6개 영역을 확인함
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if Pillar[i][j] and checkPillar(i, j) == False:
                return False
            if Bar[i][j] and checkBar(i, j) == False:
                return False
    return True

def solution(n, build_frame):
    global Pillar, Bar
    
    Pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    
    # kind -> 구조물의 종류(0 기둥, 1 보), cmd -> 설치 삭제 여부(0 삭제, 1 설치)
    for x, y, kind, cmd in build_frame:
        # 기둥의 경우
        if kind == 0:
            if cmd == 1:
                if checkPillar(x, y):
                    Pillar[x][y] = 1
            else:
                Pillar[x][y] = 0
                if not canDelete(x, y):
                    Pillar[x][y] = 1
        # 보의 경우
        else:
            if cmd == 1:
                if checkBar(x, y):
                    Bar[x][y] = 1
            else:
                Bar[x][y] = 0
                if not canDelete(x, y):
                    Bar[x][y] = 1
                
    answer = []
    
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                answer.append([x,y,0])
            if Bar[x][y]:
                answer.append([x,y,1])
    
    return answer
#feat(Jeongmu-Jo): [카카오, 2020블라인드] 자물쇠와 열쇠
