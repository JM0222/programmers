import math
def cluster(str):
    answer = []
    alphabet = [
      "A",
      "B",
      "C",
      "D",
      "E",
      "F",
      "G",
      "H",
      "I",
      "J",
      "K",
      "L",
      "M",
      "N",
      "O",
      "P",
      "Q",
      "R",
      "S",
      "T",
      "U",
      "V",
      "W",
      "X",
      "Y",
      "Z",
    ];
    words = ''
    for i in str:
        if (i.upper() in alphabet):
            words += i.upper()
    for i in range(len(words)-1):
        word = words[i:i+2]
        answer.append(word)
    return answer

def solution(str1, str2):
    result = 0 
    word_a = cluster(str1)
    word_b = cluster(str2)
    newWord = word_a + word_b
    commonWord = set(word_a) & set(word_b)
    if (sorted(word_a) == sorted(word_b)):
        result = 1
    else:
        print(sorted(word_a), sorted(word_b))
        result = (len(commonWord) / (len(newWord) - len(commonWord))) 

    result = math.trunc(result * 65536)
    return result
print(solution('aa1+aa2','AAAA12'))