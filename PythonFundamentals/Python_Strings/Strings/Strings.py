class Strings:
    def strings_intro(self):
        # String Concatenation
        s = "GfG"
        s2 = s + s[0]
        print(s2)

        # Indexing in string both positive and negative
        word = "GeeksforGeeks"
        # G     e      e       k       s       f       o       r       G       e       e       k       s
        # -13   -12    -11     -10     -9      -8      -7      -6       -5     -4       -3      -2      -1
        # 0     1       2       3       4      5        6       7       8       9       10      11      12
        # Negative Indexing
        print(word[-4])

        # Slicing
        a1 = word[0:7]
        # Retrieves characters from beginning to index 3: 'Geek'
        a2 = word[:4]
        # Retrieves characters from index 5 to the end
        a3 = word[5:]
        # Reverse a string
        a4 = word[::-1]

        print(a1)
        print(a2)
        print(a3)
        print(a4)

        # Updating of String
        s = "updating a String"
        s1 = "U" + s[1:]
        print(s1)

        # Deleting a string
        del s

        # Length of String
        great_words = "Success isn't always about greatness"
        s2 = len(great_words)
        print(s2)

        # upper and lower case
        b1 = "manikanta"
        b2 = b1.upper()
        print(b2)

        b3 = "MYSORE"
        b4 = b3.lower()
        print(b4)

        # strip
        a2 = "  Python  "
        print(a2.strip())

        # replace
        a3 = "Python is tough to crack"
        a4 = a3.replace("tough to crack", "fun to work")
        print(a4)

        # Concatenate
        a5 = "Javascript"
        a6 = "is a"
        a7 = "scripting language"
        a8 = a5 + " " + a6 + " " + a7
        print(a8)

        # Repeat
        a10 = "Javascript "
        a11 = a10 * 3
        print(a11)

        # in Keyword
        b5 = "Never mind the words of those who insult you"
        print("insult" in b5)
        print("flowers" in b5)


class_Strings = Strings()
class_Strings.strings_intro()
