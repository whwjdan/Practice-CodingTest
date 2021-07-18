def solution(msg) :
    answer = []
    al_dict = {}
    idx_s = 0
    idx_en = 1

    for i in range(26) :
        al_dict[chr(ord('A') + i)] = i

    while idx_s < len(msg) :

        while msg[idx_s:idx_en] in al_dict and idx_en <= len(msg) :
            idx_en += 1

        answer.append(al_dict[msg[idx_s:idx_en-1]] + 1)

        al_dict[msg[idx_s:idx_en]] = len(al_dict)

        idx_s = idx_en - 1
        idx_en += 1

    return answer

#feat(Jeongmu-Jo): [카카오, 2018블라인드] 압축
