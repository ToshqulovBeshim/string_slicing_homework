def main(s):
    """
    The s string variable is given. return the four characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=""
    for i in range(len(s)):
        a+=s[i]+"   "
    return a[0:10:2]

s="codectbtbiun"
print(main(s))