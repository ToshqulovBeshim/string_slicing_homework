def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    return s[n:k:]
n=3
k=6
s="sdfghjuytres"
print(main(s,n,k))