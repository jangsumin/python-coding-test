from collections import deque
def solution(bridge_length, weight, truck_weights):
    current_bridge = deque()
    times = deque()
    
    i = 0
    trucks = deque(truck_weights)
    while True:
        if len(trucks) == 0:
            break
        
        if current_bridge and times and i == times[0]:
            current_bridge.popleft()
            times.popleft()
                
        if sum(current_bridge) + trucks[0] <= weight:
            current_bridge.append(trucks.popleft())
            times.append(i + bridge_length)
        i += 1
    
    return i + bridge_length