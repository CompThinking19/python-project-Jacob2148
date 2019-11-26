#An attempt at creating a text adventure and escape room
#Plan to have the user/player start in one area and try to make their way through a house for necessary things
#Also considering to have something equivalent to a code that would allow for the user/player to start with a required item to leave
# def(main)
#     inventory = ["wallet", "driver license"]
#     #starting equipment in the game
#     user_stuff = [inventory]
#     "pick up" = add_to_inventory
#     #define a function to allow for items to be picked up and added to the inventory
#         if element is "pick up"
#             "pick up" = True
#             #Listed as true to prove the player does have a certain item found or already in their inventory
#         else raise TyperError("I can not do that")
#
# def(search)
# #define a function to allow user to look through items in the environment
#     check_object = True
#      if nothing_found Raise TypeError("Nothing Found")
#      #Type error introduced to let the user know nothing was found
# "inventory" == inventory



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
        "yes" = query_yes_no("Do you want to pick up the flashlight")
            if True:
                "yes" = query_yes_no("you pick up the flashlight.  Did you want to take the piece of paper")
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
                    else False
                    Flashlight = False
                        "yes" = "you do not have the flashlight"
            elif:
                raise TypeError = "I can not do that"
query_yes_no("you walk to the gate and see a pad with numbers on it.  Do you want tp type in the code")
    if True:
        "yes" = "you type in the code and open the gate. You have made it outside of the property"
    else False:
        "no" = "you chose not to enter the code"
        Code = False
    else False:
        "yes" = "you do not know the code"
    elif
        raise TypeError = "I can not do that"
