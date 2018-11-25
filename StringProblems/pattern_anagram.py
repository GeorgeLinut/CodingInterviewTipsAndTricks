def compare(d1, d2):
    for k in d1.keys():
        if k not in d2:
            return False
        if d1[k] != d2[k]:
            return False
    return True


def find_anagram_position(text, p):
    if len(p) > len(text) or len(text) == 0 or len(p) == 0:
        return ":P"

    dp = {}
    window_d = {}
    index = 0
    while index < len(p):
        if p[index] in dp.keys():
            dp[p[index]] += 1
        else:
            dp[p[index]] = 1
        if text[index] in window_d.keys():
            window_d[text[index]] += 1
        else:
            window_d[text[index]] = 1
        index += 1
    if compare(window_d, dp):
        print(index - len(p), end="")

    while index < len(text):
        if window_d[text[index - len(p)]] > 1:
            window_d[text[index - len(p)]] -= 1
        else:
            window_d.pop(text[index - len(p)])
        if text[index] in window_d.keys():
            window_d[text[index]] += 1
        else:
            window_d[text[index]] = 1

        if compare(window_d, dp):
            print(index - len(p) + 1, end="")
        index += 1


find_anagram_position("AAABABAA", "AABA")
print()
print("***")
find_anagram_position("BACDGABCDA", "ABCD")

