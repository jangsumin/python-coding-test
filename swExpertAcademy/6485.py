# 삼성시의 버스 노선(D3)

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    bus_tracks = []
    for _ in range(n):
        bus_tracks.append(list(map(int, input().split())))
    p = int(input())
    stop_nums = []
    for _ in range(p):
        stop_nums.append(int(input()))
    
    res = []
    for i in range(len(stop_nums)):
        cnt = 0
        for j in range(len(bus_tracks)):
            if bus_tracks[j][0] <= stop_nums[i] <= bus_tracks[j][1]:
                cnt += 1
        res.append(cnt)
    print(f'#{t}', end=' ')
    print(*res)