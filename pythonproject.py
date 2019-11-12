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
