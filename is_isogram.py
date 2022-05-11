def is_isogram(string):
    isogram = string.lower()
    if len(isogram) == len(set(isogram)):
        return True
    else:
        return False
