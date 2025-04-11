def list_of_fruits():
    #  Creation of List
    fruits = ['Orange', 'Apple', 'Grapes', 'Watermelon', 'Papaya']
    print(fruits)

    print("")
    #  Accessing elements of a List
    print(fruits[3])
    print(fruits[4])

    print("")
    # Modifying Elements of a List
    fruits[0] = 'Mango'
    print(fruits)

    print("")
    # Adding Elements at the last
    fruits.append('Banana')
    print(fruits)
    print("")
    fruits.insert(3, 'DragonFruit')  # Inserts at Index position
    print(fruits)

    print("")
    # Removing elements from the List
    fruits.remove('Papaya')  # Removes the elements from the list
    print(fruits)
    print("")
    fruits.pop()  # Removes last element
    print(fruits)
    print("")
    del fruits[3]  # Deleting the element using the Index
    print(fruits)

    print("")
    # Iterating the list
    for i in fruits:
        print(i)

    print("")
    # List Comprehension
    new_list = [x for x in fruits]
    print(new_list)


list_of_fruits()
