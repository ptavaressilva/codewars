def duplicate_count(text):
    # count duplicated letters and digits

    characters = {}

    # count character occurrences
    for i in range(0, len(text)):
        letter = text[i].lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1

    # count keys with value greater than 1

    duplicated = 0
    for key in characters:
        if characters[key] > 1:
            duplicated += 1

    return duplicated


print(duplicate_count(""))  # 0
print(duplicate_count("abcde"))  # 0
print(duplicate_count("abcdeaa"))  # 1
print(duplicate_count("abcdeaB"))  # 2
print(duplicate_count("Indivisibilities"))  # 2
