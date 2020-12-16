while True:

    ## Handling the first set of Options
    prompt_1 = "Select an Action:\n- Eat\n- Explore\n- Sleep\n- Quit\n"
    ## Converting misinputs into usable code
    action = input(prompt_1).lower().replace(" ", "")
    ## Checking to see if the user wants to quit
    if action == 'quit':
        break
    ## Giving 'Explore' its list of actions
    elif (action == 'explore'):
        prompt_2 = "Select a direction:\n- North\n- East\n- South\n- West\n- Qutit\n"
        ## Converting misinputs into usable code
        direction = input(prompt_2).lower().replace(" ", "")
        if direction == 'quit':
            break
        elif (direction == 'north'):
            print("You went North")
        elif (direction == 'east'):
            print("You went East")
        elif (direction == 'south'):
            print("You went South")
        elif (direction == 'west'):
            print("You went West")
        else:
            print("Please repeat")
    ## Giving 'Eat' its list of actions
    elif (action == 'eat'):
        prompt_3 = "Select Food:\n- Berries\n- Onigiri\n- Sandwich\n- Qutit\n"
        ## Converting misinputs into usable code
        food = input(prompt_3).lower().replace(" ", "")
        if food == 'quit':
            break
        elif (food == 'berries'):
            print("You ate some Berries")
        elif (food == 'onigiri'):
            print("You ate an Onigiri (Rice Ball)")
        elif (food == 'sandwich'):
            print("You ate a Sandwich")
        else:
            print("Please repeat")
    ## Giving 'Sleep' its list of actions
    elif (action == 'sleep'):
        prompt_4 = "How long do you want to sleep for:\n- 2 Hours\n- 4 Hours\n- 6 Hours\n- 8 Hours\n- Qutit\n"
        ## Converting misinputs into usable code
        length = input(prompt_4).lower().replace(" ", "")
        if length == 'quit':
            break
        elif (length == '2hours'):
            print("You slept for 2 Hours!")
        elif (length == '4hours'):
            print("You slept for 4 Hours!")
        elif (length == '6hours'):
            print("You slept for 6 Hours!")
        elif (length == '8hours'):
            print("You slept for 8 Hours!")
        else:
            print("Please repeat")
