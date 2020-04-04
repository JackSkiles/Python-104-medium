
# Takes user input for phrase to incript.
user_phrase = input('Enter phrase: ').upper()

# Creates alphebet variable that stores the alphebet and split them after each ','.
alphebet = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')

# Creates final_phrase variable that stores the final phrase after the loop.
final_phrase = ''

# Creates loop that should take user input and move it 13 place to the right based on the alphebet variable. It also adds a space at the beggining of each loop.
for i in range(len(user_phrase)):
    final_phrase += ' '
    if user_phrase[i] == alphebet[0]:
        final_phrase += alphebet[13]
    elif user_phrase[i] == alphebet[1]:
        final_phrase += alphebet[14] 
    elif user_phrase[i] == alphebet[2]:
        final_phrase += alphebet[15] 
    elif user_phrase[i] == alphebet[3]:
        final_phrase += alphebet[16] 
    elif user_phrase[i] == alphebet[4]:
        final_phrase += alphebet[17] 
    elif user_phrase[i] == alphebet[5]:
        final_phrase += alphebet[18] 
    elif user_phrase[i] == alphebet[6]:
        final_phrase += alphebet[19] 
    elif user_phrase[i] == alphebet[7]:
        final_phrase += alphebet[20] 
    elif user_phrase[i] == alphebet[8]:
        final_phrase += alphebet[21] 
    elif user_phrase[i] == alphebet[9]:
        final_phrase += alphebet[22] 
    elif user_phrase[i] == alphebet[10]:
        final_phrase += alphebet[23]
    elif user_phrase[i] == alphebet[11]:
        final_phrase += alphebet[24] 
    elif user_phrase[i] == alphebet[12]:
        final_phrase += alphebet[25] 
    elif user_phrase[i] == alphebet[13]:
        final_phrase += alphebet[0] 
    elif user_phrase[i] == alphebet[14]:
        final_phrase += alphebet[1] 
    elif user_phrase[i] == alphebet[15]:
        final_phrase += alphebet[2] 
    elif user_phrase[i] == alphebet[16]:
        final_phrase += alphebet[3] 
    elif user_phrase[i] == alphebet[17]:
        final_phrase += alphebet[4] 
    elif user_phrase[i] == alphebet[18]:
        final_phrase += alphebet[5] 
    elif user_phrase[i] == alphebet[19]:
        final_phrase += alphebet[6] 
    elif user_phrase[i] == alphebet[20]:
        final_phrase += alphebet[7] 
    elif user_phrase[i] == alphebet[21]:
        final_phrase += alphebet[8] 
    elif user_phrase[i] == alphebet[22]:
        final_phrase += alphebet[9] 
    elif user_phrase[i] == alphebet[23]:
        final_phrase += alphebet[10] 
    elif user_phrase[i] == alphebet[24]:
        final_phrase += alphebet[11] 
    elif user_phrase[i] == alphebet[25]:
        final_phrase += alphebet[12] 
print(final_phrase)