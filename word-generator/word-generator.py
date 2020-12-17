import random

vowel = ['a', 'e', 'i', 'o', 'u', 'y']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']

def generate_word(length):
    generated_word = ''
    # define to start with vowel or consonant
    random.seed()
    start_with = random.choice(['vowel', 'consonant'])
    generated_word += random.choice(vowel if (start_with == 'vowel') else consonant)
    previous_letter = start_with
    for current_letter in range(1, length):
        # we already have first letter
        generated_word += random.choice(consonant if (previous_letter == 'vowel') else vowel)
        previous_letter = 'consonant' if (previous_letter == 'vowel') else 'vowel'
    return generated_word

random.seed()
for x in range(8):
    print(generate_word(random.randint(3, 15)))