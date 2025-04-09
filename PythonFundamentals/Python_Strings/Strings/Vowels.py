def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0  # Initialize the vowel counter
    for char in s:  # Loop through each character in the string
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the counter if it's a vowel
    return count  # Return the final count


input_string = "Hello, World!"
print("Number of vowels:", count_vowels(input_string))
