def calculate_vowel_sum(text):
    vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    total_sum = 0

    for char in text:
        if char.lower() in vowels:
            total_sum += vowels[char.lower()]

    return total_sum


text = input()
result = calculate_vowel_sum(text)
print(result)
