from typing import List
from bisect import bisect_left, bisect_right
def solution(words, queries):
    words_by_length = [[] for _ in range(10001)]
    reversed_words_by_length = [[] for _ in range(10001)] 
    
    for word in words:
        words_by_length[len(word)].append(word)
        reversed_words_by_length[len(word)].append(word[::-1])
    
    words_by_length = [sorted(i) for i in words_by_length]
    reversed_words_by_length = [sorted(i) for i in reversed_words_by_length]
    result = []
    for query in queries:
        if query[0] == "?":
            query = query[::-1]
            res = count_match_word(reversed_words_by_length[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        else:
            res = count_match_word(words_by_length[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        result.append(res)
    return result

def count_match_word(words: List, left_value: int, right_value: int):
    left_idx = bisect_left(words, left_value)
    right_idx = bisect_right(words, right_value)

    return right_idx - left_idx

if __name__ == "__main__":
    assert solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]) == [3, 2, 4, 1, 0]