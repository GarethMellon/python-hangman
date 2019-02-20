
list_query = ['j', 'a', 'z', 'z']
state_play = ['*', '*', '*', '*']

letter = "z"

test_char = 3


game_loop = 0
incorect = 0

while game_loop < 4:

    print("letter: " + letter)
    
    if letter == '99':
        break
    
    if letter in list_query:
        match_position = list_query.index(letter)

    # interate over the length of state play.  Check the the match = position and chenage letter
        pos = 0
        while pos < len(state_play):
            if pos == match_position:
                state_play[pos] = letter
                continue
            pos += 1
        
        print(state_play)
    else:
        # here is where you build you handman
        print("no match")
        incorect += 1
        if incorect == 2:
            print("Game Over")
            break
        
    game_loop += 1
