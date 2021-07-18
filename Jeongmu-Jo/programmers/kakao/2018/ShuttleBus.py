def solution(n, t, m, timetable):
    time_list = []
    for time in timetable:
        minute = int(time[:2]) * 60 + int(time[3:])
        time_list.append(minute)

    time_list.sort()

    bus_time = 9 * 60
    time_dict = {}
    for i in range(n):
        waiting_list = []
        for j in range(m):
            if len(time_list) != 0 and time_list[0] <= bus_time:
                waiting_list.append(time_list.pop(0))
            else:
                break
        time_dict[bus_time] = waiting_list

        bus_time = bus_time + t

    bus_time = bus_time - t

    if len(time_dict[bus_time]) < m:
        result = bus_time
    else:
        result = max(time_dict[bus_time]) - 1

    result = "{:02d}:{:02d}".format(int(result/60), result%60)

    return result

#feat(Jeongmu-Jo): [카카오, 2018블라인드] 셔틀버스
