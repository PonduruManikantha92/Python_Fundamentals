class max_n_min_numbers():
    def built_in_methods(self):
        numbers = [12, 45, 2, 89, 5, 34, 77]

        maximum = max(numbers)
        minimum = min(numbers)

        print("Maximum number is:", maximum)
        print("Minimum number is:", minimum)

    def check_max_n_min_numbers(self):
        numbers = [12, 45, 2, 89, 5, 34, 77]

        max_num = numbers[0]
        min_num = numbers[0]

        for num in numbers:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num

        print("Maximum number is:", max_num)
        print("Minimum number is:", min_num)


testing = max_n_min_numbers()
testing.built_in_methods()
testing.check_max_n_min_numbers()


