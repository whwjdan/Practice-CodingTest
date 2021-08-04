def solution(record):
    answer = []
    dicts = {}
    for i in record:
        r = i.split(' ')
        if r[0] == "Enter":
            dicts[r[1]] = r[2]
        elif r[0] == "Change":
            dicts[r[1]] = r[2]
            
    for i in record:
        r = i.split(' ')
        if r[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(dicts[r[1]]))
        elif r[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(dicts[r[1]]))
    return answer

#feat(Jeongmu-Jo): [카카오, 2019블라인드] 오픈채팅방
