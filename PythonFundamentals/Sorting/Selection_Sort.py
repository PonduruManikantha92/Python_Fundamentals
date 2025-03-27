class Selection:
    def sort_test(self):
        options = [8, 22, 7, 9, 31, 5, 13]  # List to be sorted
        n = len(options)  # Length of the list

        for i in range(n - 1):  # Loop through the list (n-1 passes)
            min_index = i  # Assume the first unsorted element is the smallest [min_index = 0,1,2,3,4,5]

            # Find the smallest element in the remaining unsorted array
            for j in range(i + 1, n):
                if options[j] < options[min_index]:  # If a smaller element is found
                    min_index = j  # Update min_index to new smallest element

            # Swap the smallest found element with the first element of the unsorted part
            options[i], options[min_index] = options[min_index], options[i]

            print(options)  # Print the list after each pass


# Create an instance of the Selection class
testing = Selection()
testing.sort_test()
