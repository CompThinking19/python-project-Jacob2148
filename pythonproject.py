#README
#An attempt at creating a text adventure and escape room
#Plan to have the user/player start in one area and try to make their way through a house for necessary things
#premise of the program is for the user to guide themselves throughout the building and out of the small courtyard through a gate
#throughout the program a variety of actions will be asked if the user wants to participate in certain actions as they navigate through the house
#answering yes or no will cause the user to progress further or keep them in their current state
#after acquiring specific items they will be able to complete the objective of leaving the property
#yes and no as answers from the user to accomplish an action or not

def query_yes_no(question, default="yes")
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [yes/no] "
    elif default == "yes":
        prompt = " [YES/no] "
    elif default == "no":
        prompt = " [yes/NO] "
    else:
        raise value error("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Respond with 'yes' or 'no'""(or 'y' or 'n').\n")
#function to allow for yes and no responses when prompted with an applicable question
query_yes_no("open the door")
    if True:
        "yes" = "You go through the door"
    else False:
        "no" = "you stand by the door"
    elif False:
        raise TypeError = "I can not do that"

#user's input will dictate the action taken by the avatar
query_yes_no("as you go through the door, you enter a hallway. Towards the end of the hallway you see a door. Do you want to walk towards the door")
    if True:
        "yes" = "You walk towards the end of the hallway and stand at the door at the end"
    else False:
        "no" = "you stay where you are"
    elif:
        raise TypeError = "I can not do that"
query_yes_no("standing at the door you notice a table next to it with a piece of paper and a flashlight. Did you want to investigate further")
    if True:
#added variables depending on player's actions
        "yes" = query_yes_no("Do you want to pick up the flashlight")
            if True:
                "yes" = query_yes_no("you pick up the flashlight.  Did you want to take the piece of paper")
#depends on if player is accepting to take both items
Flashlight = True
            else False:
                "no" = query_yes_no("you leave the flashlight on the table.  Did you want to pick up the piece of paper")
            elif:
                raise TypeError = "I can not do that"
                    if True:
                        "yes" = "you pick up the piece of paper which has the the numbers 0451."
                    else False:
                        "no" = "you leave the paper on the table"
                    elif:
                        raise TypeError = "I can not do that"
Query_yes_no("Do you want to go through the main door")
    if True:
        "yes" = query_yes_no("you walk through the main door and see that its too dark to see outside, Did you want to turn on the flashlight")
            if True:
                "yes" = "You turn on the flashlight and can see a gate a short distance away"
            else False:
                "no" = "You still can not see"
                else False:
                    Flashlight = False
#added variable depending on if the user has the flashlight
                        "yes" = "you do not have the flashlight"
            elif:
                raise TypeError = "I can not do that"
query_yes_no("you walk to the gate and see a pad with numbers on it.  Do you want tp type in the code")
    if True:
        "yes" = "you type in the code and open the gate. You have made it outside of the property"
    else False:
        "no" = "you chose not to enter the code"query_yes_no("do you want to head back inside thew house")
            if True:
                "yes" = "You walk back inside the House"
            else False:
                Raise TypeError = "You need to go back"
        Code = False
    else False:
#added variable  depending on if the user picked up the code earlier
        "yes" = "you do not know the code."query_yes_no("do you want to head back inside the house")
    elif
        raise TypeError = "You need to go back"
#have both options after you need to go back string revert back to being at the main door by the table to collect missing item(s)
