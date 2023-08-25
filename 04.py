def solution(want, number, discount):
    answer = 0
    end_index = len(discount) - sum(number) + 1
    new_want = []

    for i in range(len(want)):
        new_want += [want[i]] * number[i]
    for i in range(end_index):
        new_arr = discount[i : i + sum(number)]
        if sorted(new_arr) == sorted(new_want):
            answer += 1
    return answer
