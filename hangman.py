from random import choice #ALL HIS


"""
select answer to check against
"""
# candidateWords is a list of possible test strings.
candidateWords = ['embezzle', 'equip', 'fjord', 'flapjack', 'flyby', 
                  'jazz', 'kayak', 'numbskull', 'basketball', 'football']


query = choice(candidateWords)    # Select the query word from the candidate list.  #ALL HIS
# Set up state_play to be an array as long as the query word initially all '*'
print("Query: " + query)

"""
print query into a list so we can check each letter with user input
"""
list_query = list(query)
print(list_query)

"""
take the query (answer) and *** out all the letters
"""
state_play = []
for letter in query:
    state_play.append('*')
    
print(state_play)

"""
function to take user input and return value
"""
def test_char():   #ALL HIS
    test_char = input("What is your guess:")
    return test_char


"""
checking is a letter is in out list query
"""

game_loop = 0
incorect = 0

while game_loop < 10:
    
    letter = test_char()
    print("letter: " + letter)
    
    if letter == '99':
        break
    
    if letter in list_query:
        match_position = list_query.index(letter) # we are checking for the index postion for out letter match
        ##list_query.remove(letter) ### now we are removing the letter from out query so we dont match it again
        

    # interate over the length of state play.  Check the the match = position and chenage letter
        pos = 0
        while pos < len(state_play):
            if pos == match_position:
                state_play[pos] = letter
            pos += 1
        
    else:
        # here is where you build you handman
        print("no match")
        incorect += 1
        if incorect == 2:
            print("Game Over")
            break
        
    game_loop += 1
