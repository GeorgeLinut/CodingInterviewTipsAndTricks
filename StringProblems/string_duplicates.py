def rem_dup(text):
    d = {}
    res = ""
    for ch in text:
        if ch not in d.keys():
            d[ch] = 1
            res += ch
        else:
            d[ch] += 1
    return res

