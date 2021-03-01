def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    
    res = []
    string = ''

    currChar = ''
    for char in text:
        
        if currChar != char:
            currChar = char
            res.append(currChar)
            res.append(1)
        else:
            index = len(res) - 1

            res[index] = res[index] + 1 
    
    while len(res) > 0:
        string = string + res.pop(0) + str(res.pop(0))

    return string.replace("1", "")
        
        
def printAmount(char, count):
    string = ''
    for index in range(int(count)):
        string = string + char
    return string


def decode(text):
    """
    Decodes the text using run-length encoding
    """
    string = ''

    currChar = ''
    amount = 1
    for char in text:

        if char.isnumeric():
            amount = int(char) - 1
        else:
            currChar = char
            amount = 1
        string = string + printAmount(currChar, amount)
    
    return string

print(decode("A2BC3DE4"))


# Tests
# Test that the functions work on their own
assert encode("AABCCCDEEEE") == "A2BC3DE4"
assert decode("A2BC3DE4") == "AABCCCDEEEE"

# Test that the functions really invert each other
assert decode(encode("AABCCCDEEEE")) == "AABCCCDEEEE"
assert encode(decode("A2BC3DE4")) == "A2BC3DE4"