class Bubble:
    def sort_test(self):
        options = [8, 22, 7, 9, 31, 5, 13]
        n = len(options)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if options[j] > options[j + 1]:
                    options[j], options[j + 1] = options[j + 1], options[j]
                    swapped = True
            if not swapped:
                break
            print(options)


testing = Bubble()
testing.sort_test()
