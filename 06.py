numbers = [2, 3, 3, 5]


# result [3, 5, 5, -1]
# [9, 1, 5, 3, 6, 2][-1, 5, 6, 6, -1, -1]
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


(solution(numbers))
