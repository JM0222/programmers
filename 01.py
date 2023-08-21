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
    
    for i in range(len(str)-1):
        word = str[i:i+2].upper()
        if ((word[0] in alphabet) & (word[1] in alphabet)):
            answer.append(word)
    return answer

def solution(str1, str2):
    result = 0 
    word_a = cluster(str1)
    word_b = cluster(str2)
    newWord = word_a + word_b
    commonWord = []
    for i in word_b:
        if i in word_a:
                word_a.remove(i)
                commonWord.append(i)
    if (sorted(word_a) == sorted(word_b)):
        result = 1
    else:
        result = (len(commonWord) / (len(newWord) - len(commonWord))) 

    result = math.trunc(result * 65536)
    return result