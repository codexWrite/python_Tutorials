# match case
a = input("Enter the character.")
match(a):
    case 'a' | 'i' | 'e' | 'o' | 'u':
        print("Vowel")
    # case 'e':
    #     print("Vowel")
    # case 'i':
    #     print("Vowel")
    # case 'o':
    #     print("Vowel")
    # case 'u':
    #     print("Vowel")
    case _:
        print("consonent")