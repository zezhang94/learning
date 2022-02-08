from collections import deque

class MLESolution:
    def racecar(self, target: int) -> int:
        queue = deque()
        # (positon, speed, depth)
        queue.append((0, 1, 0))
        while len(queue) > 0:
            position, speed, depth = queue.pop()
            if position == target:
                return depth
            queue.appendleft((position + speed, speed * 2, depth + 1))
            speed = -1 if speed > 0 else 1
            queue.appendleft((position, speed, depth + 1))

solution = MLESolution()

#print(solution.racecar(3))
print(solution.racecar(6))

            