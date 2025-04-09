def integers(s):
    count = 0
    for i in s:
        if i % 2 == 0:
            count += 1
    return count


input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integers(input_values))
