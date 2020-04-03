
# Prompts user for phrase input
user_input = input('Please enter a phrase of your choosing: ').upper()
# Creates an emtpy string to add phrase pieces to
full_phrase = ''

# Should loop through the rang of the users input one point at a time, replacing any string with a new string.
for i in range(len(user_input)):
   if user_input[i] == 'A':
       full_phrase += '4' 
   elif user_input[i] == 'E':
       full_phrase += '3' 
   elif user_input[i] == 'G':
       full_phrase += '6'
   elif user_input[i] == 'I':
       full_phrase += '1'
   elif user_input[i] == 'O':
       full_phrase += '0'
   elif user_input == 'S':
       full_phrase += '5'
   elif user_input[i] == 'T':
       full_phrase += '7'
   else:
       full_phrase += user_input[i]
print(full_phrase)