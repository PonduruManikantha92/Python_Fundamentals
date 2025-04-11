def multiples():
    empty_list = []
    for i in range(100):
        if i % 3 == 0:
            empty_list.append(i)
            print(i)


multiples()
