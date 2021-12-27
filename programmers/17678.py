def solution(n, t, m, timetable):
    bus_arrive = [[9, 0]]
    time = [9, 0]
    for i in range(n-1):
        time[1] += t
        if time[1] >= 60:
            time[0] += (time[1] // 60)
            time[1] = time[1] % 60
        bus_arrive.append(time)
    
    timetable = [list(map(int, i.split(":"))) for i in timetable]
    timetable.sort()
    bustable = {}

    for hour, minute in bus_arrive:
        people = 0
        end_line = 0
        bustable[f"{hour:02}:{minute:02d}"] = []
        for idx, (p_h, p_m) in enumerate(timetable):
            if p_h < hour or (p_h == hour and p_m <= minute):
                people += 1
                end_line = idx
                bustable[f"{hour:02}:{minute:02}"].append([p_h, p_m])
                if people == m:
                    break
        timetable = timetable[end_line+1:]
    
    print(bustable)
    for idx, (key, value) in enumerate(bustable.items()):
        if idx == len(bustable)-1:
            if len(value) < m:
                return key
            else:
                hour, minute = value[-1]
                minute -= 1
                if minute < 0:
                    hour -= 1
                    minute = 60 + minute
                return f"{hour:02}:{minute:02}"
    


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60	, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))