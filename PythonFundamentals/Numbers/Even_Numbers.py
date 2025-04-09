def integers(s):
    results = []
    count = 0
    for i in s:
        if i % 2 == 0:
            count += 1
            results.append(i)
    return results


input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integers(input_values))
