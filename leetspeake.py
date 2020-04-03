user_input = input('Please enter a phrase of your choosing: ').upper()
full_phrase = ''

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