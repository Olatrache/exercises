vowel = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U')
char = input('input a character : ')

if char in vowel:
    print(char, 'is a vowel')
else:
    print(char, 'is a consonant')