"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is
present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    word_list = sentence.split()
    result = ''
    if len(word_list[0]) > 4:
        for k in word_list[0][::-1]:
            result += k
    else:
        result += word_list[0]
    for i in word_list[1:]:
        if len(i) > 4:
            result += ' '
            for j in i[::-1]:
                result += j
        else:
            result += ' ' + i
    return result

print(spin_words("Welcome"))
