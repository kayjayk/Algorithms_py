def dfs(idx, summary, numbers, target):
    res = 0
    if idx == len(numbers):
        if summary == target:
            return 1
        else:
            return 0

    res += dfs(idx+1, summary + numbers[idx], numbers, target)
    res += dfs(idx+1, summary - numbers[idx], numbers, target)

    return res

def solution(numbers, target):
    answer = 0
    answer = dfs(0, 0, numbers, target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))