#An attempt at creating a text adventure and escape room
#Plan to have the user/player start in one area and try to make their way through a house for necessary things
#Also considering to have something equivalent to a code that would allow for the user/player to start with a required items to leave
def(main)
    inventory = ["wallet", "driver license"]
    #starting equipment in the game
    user_stuff = [inventory]
    "pick up" = add_to_inventory
    #define a function to allow for items to be picked up and added to the inventory
        if element is "pick up"
            "pick up" = True
            #Listed as true to prove the player does have a certain item found or already in their inventory
        else raise TyperError("I can not do that")

def(search)
#define a function to allow user to look through items in the environment
    check_object = True
     if nothing_found Raise TypeError("Nothing Found")
     #Type error introduced to let the user no nothing was found
