def odd_number_count(s):
    count = 0
    for i in s:
        if i % 2 != 0:
            count += 1
    return count


def odd_numbers(s1):
    count = 0
    list_of_odds = []
    for i in s1:
        if i % 2 != 0:
            count += 1
            list_of_odds.append(i)
    return list_of_odds


input_values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(odd_number_count(input_values))
print(odd_numbers(input_values))
