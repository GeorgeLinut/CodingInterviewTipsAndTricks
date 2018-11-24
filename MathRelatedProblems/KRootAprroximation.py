function root(x, n, error):
    if (x == 0):
        return 0

    left = 0
    right = max(1, x)
    middle = (right + left) / 2

    while (middle - left >= error):
        if (power(middle, n) > x):
            right = middle
        else if (power(middle, n) < x):
            left = middle
        else
            break

        middle = (right + left) / 2

    return middle