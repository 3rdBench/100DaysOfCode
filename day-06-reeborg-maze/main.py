# Right turn function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Perform the following actions while searching for the exit (i.e. goal)
while not at_goal():
    # Check if Reeborg's right side is clear, turn right & move forward 1-step
    if right_is_clear():
        turn_right()
        move()
    # Check if Reeborg's front size is clear & move forward 1-step 
    elif front_is_clear():
        move()
    else:
        # Otherwise turn Reeborg to the left
        turn_left()