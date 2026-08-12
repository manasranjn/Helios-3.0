sentence = input('Enter a Sentece: ')

words = sentence.split(' ')

print(len(words))

vowels = 0
consonants = 0

for char in sentence:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1

print(f'Vowels: {vowels}')
print(f'Consonants: {consonants}')