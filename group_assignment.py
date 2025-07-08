#assignment 1
def count_vowels(word):
    counter = 0

    for i in word:
        if i in "aeiouAEIOU":
            counter += 1

    print(counter)

count_vowels("pride)")

"""========================================================"""
# assignment 2

s = input("Please enter a string you want to parse: \n")
tokens = input('please enter the key words of your string separated by a ", ": \n')

def compress_tokens(s, tokens):
    # Manually parse tokens separated by ", " using only strings
    parsed_tokens = ""
    i = 0
    while i < len(tokens):
        if i+1 < len(tokens) and tokens[i] == ',' and tokens[i+1] == ' ':
            if parsed_tokens != "":
                parsed_tokens += "|"
            i += 2
        else:
            parsed_tokens += tokens[i]
            i += 1
    # Now parsed_tokens contains tokens separated by "|"
    # Extract tokens one by one and uppercase them in s manually
    result = ""
    start = 0
    while start < len(s):
        found = False
        # For each token, check if it matches at this position
        token_start = 0
        token = ""
        while token_start < len(parsed_tokens):
            # Find next separator or end
            token_end = token_start
            while token_end < len(parsed_tokens) and parsed_tokens[token_end] != '|':
                token_end += 1
            token = parsed_tokens[token_start:token_end]
            #Ensure it is using keywords that are on their own and not part of another word (IG: butterfly will fly, with keyword fly, will return butterfly will FLY not butterFLY will FLY)
            if token != "" and s[start:start+len(token)] == token and (start == 0 or s[start-1] == ' ') and (start+len(token) == len(s) or s[start+len(token)] == ' '):
                result += token.upper()
                start += len(token)
                found = True
                break

            token_start = token_end + 1
        if not found:
            result += s[start]
            start += 1
    return result

result = compress_tokens(s, tokens)
print(f"\n Your string with keywords noted is \n {result}")


"""============================================================================"""

# 3rd challenge cypher_text aka operation get_rotated

s = input("Please enter a word, or string you wish to proccess: \n")
n = input("Please enter number of characters you wish to rotate: \n")

n = int(n) #turns it into an integer for calculations of %

def rotate_string(s, n):
    s_len = len(s)
    cypher = ""
    count = 0

    # If n is larger than the length do %
    if n > s_len:
        n = n % s_len

    # set the start point
    index = s_len - n

    while count < s_len:
        # Rebuild starting at startpoint character by character
        cypher += s[index] 
        count += 1
        index += 1
        if index == s_len:
            index = 0  # Wrap back to the start of the string
    
    return cypher


cypher = rotate_string(s, n)
print(cypher)