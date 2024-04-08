def count_vowels_consonants(s):    
    s = s.lower()
    vowels = 0
    consonants = 0
    vowel_set = set("aeiou")
    consonant_set = set("bcdfghjklmnpqrstvwxyz")
    for char in s:
        if char in vowel_set:
            vowels += 1
        elif char in consonant_set:
            consonants += 1
    return vowels, consonants
string = input("Введите строку: ")
vowels, consonants = count_vowels_consonants(string)
print('Количество гласных букв:',vowels)
print('Количество согласных букв:',consonants)
