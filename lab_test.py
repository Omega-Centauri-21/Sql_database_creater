f = open("test_file.txt", "r")
g = f.read()

def main(g):
    uppercase_count = 0
    lowercase_count = 0
    digits_count = 0
    whitespace_count = 0
    vowels = 0
    consonants = 0
    special_char  = 0

    for word in g:
        if word.isupper():
            uppercase_count += 1
        elif word.islower():
            lowercase_count += 1
        elif word.isdigit():
            digits_count += 1
        elif word.isspace():
            whitespace_count += 1
        else:
            special_char += 1

    for i in g:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print(uppercase_count , lowercase_count, digits_count, whitespace_count, vowels, consonants, special_char)

main(g)
