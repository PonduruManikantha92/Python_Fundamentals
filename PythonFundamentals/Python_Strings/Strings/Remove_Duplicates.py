def remove_duplicates(s):
    result = ""
    seen = set()    # set() creates an empty set in Python. set() creates an empty set in Python. Does not allow duplicates
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result


input_value = "Programming"
print(remove_duplicates(input_value))



