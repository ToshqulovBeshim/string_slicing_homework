def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a= s[-1:-5:-1]
    return a[::-1]
s="jeuixinxnuixux"
print(main(s))