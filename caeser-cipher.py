
# Takes user input for phrase to incript.
user_phrase = input('Enter phrase: ').upper()

# Creates alphebet variable that stores the alphebet and split them after each ','.
alphebet = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')

# Creates final_phrase variable that stores the final phrase after the loop.
final_phrase = ''

# Creates loop that should take user input and move it 13 place to the right based on the alphebet variable.
for i in range(len(user_phrase)):
    if user_phrase[i] == alphebet[0]:
        final_phrase += alphebet[13]
    elif user_phrase[i] == alphebet[1]:
        final_phrase += alphebet[14]
print(final_phrase)