"""
    this algorithm is working on characters that return number of them in unicode language world
    
    bahman ==> [98, 97, 104, 109, 97, 110]
    amir ==> [97, 109, 105, 114]

    [98, 97, 104, 109, 97, 110] ==> bahman
    [97, 109, 105, 114] ==> amir

"""

def encode(plain):
    """
    it is very simple to encode without extra things so i added a random number to show
    edited list of unicode numbers but remmember that must use that number to decode function too!
    """
    # return [ord(char) for word in plain]

    return [ord(char)-77 for char in plain]


def decode(decode_list):
    """
    it return a generator that data saved on it must use join method on a string to show a data
    """

    # return (chr(word) for word in decode_list)
    # return "".join(chr(word) for word in decode_list)
    return "".join(chr(word+77) for word in decode_list)

print(encode("bahman"))

print(decode([21, 20, 27, 32, 20, 33]))
# print(decode([98, 97, 104, 109, 97, 110]))
