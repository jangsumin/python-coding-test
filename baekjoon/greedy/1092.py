# 배

n = int(input())
limits = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

limits.sort(reverse=True)
boxes.sort(reverse=True)

if max(limits) < max(boxes):
    print(-1)
else :
    time = 0
    while boxes:
        if not boxes:
            break
        for limit in limits:
            for box in boxes:
                if limit >= box:
                    boxes.remove(box)
                    break
        time += 1
    print(time)