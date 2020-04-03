# Program is intended to add vowels to existing vowels whenever they show up in the user inputed string.
# Takes user input for a phrase or word
phrase = input('Please input a phrase or word: ')

# Changes entries to upper case for formating reasons.
phrase = phrase.upper()

# Creating variables to check for vowels
vowel_a = 'A'
vowel_e = 'E'
vowel_i = 'I'
vowel_o = 'O'
vowel_u = 'U'
vowel_y = 'Y'

# Creats an empty variable to store the statement
full_statemenet = ''

# A for loop that loops through the user statement and adds vowels accordingly.
for i in range(len(phrase)):
    if phrase[i] == vowel_a:
        full_statemenet += 'AAAAA'
    elif phrase[i] == vowel_e:
        full_statemenet += 'EEEEE'
    elif phrase[i] == vowel_i:
        full_statemenet += 'IIIII'
    elif phrase[i] == vowel_o:
        full_statemenet += 'OOOOO'
    elif phrase[i] == vowel_u:
        full_statemenet += 'UUUUU'
    elif phrase[i] == vowel_y:
        full_statemenet += 'YYYYY'
    else:
        full_statemenet += phrase[i]
print(full_statemenet)