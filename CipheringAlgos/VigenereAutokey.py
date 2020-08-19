chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def Enc(strn, key):
    # Creating key upto message length
    i = 0
    while len(key) != len(strn):
        key += strn[i]
        i += 1

    # Encrypting process
    if strn.isupper():
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) + ord(key[i])) % 26) + ord('A')
            st += chr(s)
        return st

    if strn.islower():
        strn = strn.upper()
        key = key.upper()
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) + ord(key[i])) % 26) + ord('a')
            st += chr(s)
        st = st.lower()

        return st



def Dec(strn, key):
    # Creating key
    i = 0
    while len(key) != len(strn):
        key += chr(((ord(strn[i]) - ord(key[i])) % 26) + ord('A'))
        i += 1

    if strn.isupper():
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) - ord(key[i]) + 26) % 26) + ord('A')
            st += chr(s)
        return st

    if strn.islower():
        strn = strn.upper()
        key = key.upper()
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) - ord(key[i]) + 26) % 26) + ord('A')
            st += chr(s)
        st = st.lower()
        return st
