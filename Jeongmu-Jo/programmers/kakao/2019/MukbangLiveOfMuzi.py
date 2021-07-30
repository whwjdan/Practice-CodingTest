def solution(food_times, k):
    answer = 0

    sorted_list = sorted(food_times)
    sorted_list.insert(0, 0)

    len_food = len(food_times)
    break_time = 0

    for i in range(1, len(sorted_list)):
        sub = sorted_list[i] - sorted_list[i - 1]
        t = sub * len_food
        if k >= t:
            k -= t
            len_food -= 1
        else:
            break_time = sorted_list[i]
            break

    if break_time == 0:
        answer = -1
    else:
        k %= len_food
        for i in range(len(food_times)):
            if food_times[i] >= break_time:
                k -= 1
                if k == -1:
                    answer = i + 1
                    break
    return answer
    