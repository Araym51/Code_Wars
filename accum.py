"""passed"""
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper()
        result += (letter.lower() * i)
        i += 1
        if len(s) != i:
            result += '-'
    return print(result)



accum("abcd")
accum("RqaEzty")
accum("cwAt")
