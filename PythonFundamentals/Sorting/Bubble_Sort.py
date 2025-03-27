def bubble():
    options = [60, 50, 10, 40, 20]
    n = len(options)  # value of n is 5
    for i in range(n):
        # print(i)         # value of i is 0, 1, 2, 3, 4
        swapped = False  # Optimization: Track if a swap occurs
        for j in range(n - i - 1):  # (5 -0 -1) =4, (5 -1 -1) =3, (5 -2 -1) =2, (5 -3 -1) =1, (5 -4 -1) = 0
            # print(j)
            if options[j] > options[j + 1]:
                options[j], options[j + 1] = options[j + 1], options[j]
                swapped = True
        if not swapped:  # If no swaps happened, break early
            break

        print("Sorted list:", options)


bubble()
