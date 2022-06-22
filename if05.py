def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    s = 0
    x = n % 10
    if(x > s):
        s = x
    n //= 10

    x = n % 10
    if(x > s):
        s = x
    n //= 10

    x = n % 10
    if(x > s):
        s = x
    n //= 10

    x = n % 10
    if(x > s):
        s = x
    n //= 10

    x = n % 10
    if(x > s):
        s = x
    return s
