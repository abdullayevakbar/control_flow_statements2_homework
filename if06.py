def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    s = -1
    ind = -1
    x = n % 10
    if(x > s):
        s = x
        ind = 1
    n /= 10

    x = n % 10
    if(x > s):
        s = x
        ind = 2
    n /= 10

    x = n % 10
    if(x > s):
        s = x
        ind = 3
    n /= 10

    x = n % 10
    if(x > s):
        s = x
        ind = 4
    n /= 10

    x = n % 10
    if(x > s):
        s = x
        ind = 5
    return ind
