def solution(s):
    answer = []

    cnt_zero = 0
    cnt = 0
    new_word = s

    while True:
        temp_word = ""
        for i in range(len(new_word)):
            if new_word[i] == "0":
                cnt_zero += 1
            elif new_word[i] == "1":
                temp_word += "1"
        if len(temp_word) == 1:
            cnt += 1
            break
        else:
            cnt += 1
            bin_new_word = bin(len(temp_word))[2:]
            new_word = bin_new_word

    answer.append(cnt)
    answer.append(cnt_zero)
    return answer


print(solution("01110"))
