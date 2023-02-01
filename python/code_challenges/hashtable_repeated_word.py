import re



def first_repeated_word(str):
    # Create a var called split_string that uses split method on passed in string
    # create var called hashtable
    # use for loop to iterate over split_string
    # if word is not in dictionary:
    #    with words as keys and count as value
    # else word is in dictionary:
    #   return the string we are iterating over
    # return "No repeated word"
    string_lower = str.lower()
    string_lower_no_punc = re.sub(r'[^\w\s]', '', string_lower)
    split_string = string_lower_no_punc.split()
    hashtable = {}
    for word in split_string:
        if word not in hashtable:
            hashtable[word] = 1
        else:
            return word
    return None

test_string = "apple? BANANA! banana, apple."
print(first_repeated_word(test_string))




