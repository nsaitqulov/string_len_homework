def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    x=len(s)
    y="*"*len(s)
    return y
print(main("code"))