def Enc(txt, k):
    # transforming key to length of message
    ls = ""
    i = 0
    while len(ls) != len(txt):
        ls += k[i]
        if i == len(k) - 1:
            i = 0
            continue
        i += 1

    # Encrypting the message
    st = ""
    for i in range(len(txt)):
        s = ((ord(txt[i]) + ord(ls[i])) % 26) + ord('A')
        st += chr(s)

    return st


def Dec(txt, k):
    # transforming key to length of message
    ls = ""
    i = 0
    while len(ls) != len(txt):
        ls += k[i]
        if i == len(k) - 1:
            i = 0
            continue
        i += 1

    # Decrypting the message
    st = ""
    for i in range(len(txt)):
        s = ((ord(txt[i]) - ord(ls[i]) + 26) % 26) + ord('A')
        st += chr(s)

    return st