# Given an array of characters, compress the array in a way such that [aBBBAAaaa] becomes
# [a1B3A2a3].


def str_compress(a):
    if len(a) == 0:
        return None
    s = ""
    ch = a[0]
    fr = 1
    for c in a[1:]:
        if c == ch:
            fr += 1
        else:
            s += ch
            s += str(fr)
            fr = 1
            ch = c

    return s + ch + str(fr)


print(str_compress(['B', 'B', 'B', 'A', 'A', 'a', 'a', 'a']))

