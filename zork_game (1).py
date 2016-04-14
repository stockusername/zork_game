#text for game
intro_text = "Welcome to Zork, the online text-based game.  Be prepared to enter a world of fantasy and fun.  Press ENTER to start the game."
#hall text
door1_1 = "You are in a dimly lit hall on floor 1. There are five rooms in the hall, and you are in front of the first door."
door1_2 = "You are in a dimly lit hall on floor 1. There are five rooms in the hall, and you are in front of the second door."
door1_3 = "You are in a dimly lit hall on floor 1. There are five rooms in the hall, and you are in front of the third door."
door1_4 = "You are in a dimly lit hall on floor 1. There are five rooms in the hall, and you are in front of the fourth door."
door1_5 = "You are in a dimly lit hall on floor 1. There are five rooms in the hall, and you are in front of the fifth door."
door2_1 = "You are in a dimly lit hall on floor 2. There are five rooms in the hall, and you are in front of the first door."
door2_2 = "You are in a dimly lit hall on floor 2. There are five rooms in the hall, and you are in front of the second door."
door2_3 = "You are in a dimly lit hall on floor 2. There are five rooms in the hall, and you are in front of the third door."
door2_4 = "You are in a dimly lit hall on floor 2. There are five rooms in the hall, and you are in front of the fourth door."
door2_5 = "You are in a dimly lit hall on floor 2. There are five rooms in the hall, and you are in front of the fifth door."
door3_1 = "You are in a dimly lit hall on floor 3. There are five rooms in the hall, and you are in front of the first door."
door3_2 = "You are in a dimly lit hall on floor 3. There are five rooms in the hall, and you are in front of the second door."
door3_3 = "You are in a dimly lit hall on floor 3. There are five rooms in the hall, and you are in front of the third door."
door3_4 = "You are in a dimly lit hall on floor 3. There are five rooms in the hall, and you are in front of the fourth door."
door3_5 = "You are in a dimly lit hall on floor 3. There are five rooms in the hall, and you are in front of the fifth door."

#floor_1 text
nothing = "There is nothing here, you dope."
snake = "The room is bright orange and there is a massive cobra in the center. It has a human skull in its mouth."
snake_death= "The room is bright orange and a bloodied human skull lies on the floor."
stairs_up = "There is a set of crumbling stairs going up."
lazer_gun = "A lazer gun sits in a glass case."
lazer_gun_grab = "An empty glass case sits in the room."
bear_trap = '*CRACK!* That is the sound of you stepping in a bear trap. You lost your foot and are now bleeding out.'

#floor_2 text
monster = 'There is a big, ugly man named Ray in a room full of memes. He shouts, "You are in my swamp now! It is all Ogre for you boii!"'
monster_death = "You are standing in a puddle of Mountain Dew Code Red. Small flecks of burnt brains cover the meme walls."
shotgun_trap = "You are staring into the barrel of a shotgun. *BANG!* Your brains are now all over the wall. Shouldn't have opened that door."
fireballs = "There are four fireballs floating in the middle of a dusty room."
fireballs_grab = "You are standing in a dusty room."
stairs_down = "There is a set of crumbling stairs going down. The path is lit by a small torch."
stairs_up_2 = "A set of regal, carpeted stairs leads upward."

#floor_3 text 
no_floor = "There is no floor. You only notice this after you have stepped into the room, so you fall to your death and are impaled on some spikes."
stairs_down_2 = "A set of regal, carpeted stairs leads downward."
prize = "YOOOOOOOOOO! There is hella gold in here! But wait...is the gold moving? \n All the coins begin to rattle violently and move to the center of the room. \n A giant beast forms out of the coins and towers in the center of the room beating on its chest."
prize_final = "The treasure is yours! Huzzah!"
single_coin = "There is a velvety red loveseat in a blue room. A single gold coin sits on the cushion."
single_coin_grab = "There is a velvety red loveseat in a blue room."
poison_darts = "You feel a slight pinch on the side of your neck. You reach up to touch the sore spot and find a dart. You pull the dart out, examine the tip, pass out, foam at the mouth for a few minutes, and die."

#misc text



#lists to change after actions
user_items = []
defeated_foes = []


floor_1 = [nothing, snake, stairs_up, lazer_gun, bear_trap]
floor_2 = [monster, shotgun_trap, fireballs, stairs_down, stairs_up_2]
floor_3 = [no_floor, stairs_down_2, prize, single_coin, poison_darts]

#command list checks
#teleport used for testing purposes
valid_moves = ['left', 'right', 'up', 'down', 'grab', 'open', 'fight', 'leave']
grab_rooms = [4, 9, 16]
fight_rooms = [2, 7, 15]
instant_death = [5, 8, 13, 17]
stair_rooms = [3, 10, 11, 14]
hall_numbers = [0, 6, 12]

#initial setting of modifiable variables
global user_room
user_room = 0
global user_floor
user_floor = floor_1
global step
step = 1


# Our main game loop
def run_game():
    print(intro_text)
    input()
    
    game_running = True
    while game_running:
        print_player_status()
        player_move = get_user_input()
        process_move(player_move)
        game_running = check_game_status()

# Looks at the state of the game and gives information to the user about his
# Current position, bag of items, etc.
def print_player_status():
    global user_room
    global step
    global user_floor
    if user_floor == floor_1:
        if user_room == 0 and step == 1:
            print(door1_1)
        elif user_room == 0 and step == 2:
            print(door1_2)
        elif user_room == 0 and step == 3:
            print(door1_3)
        elif user_room == 0 and step == 4:
            print(door1_4)
        elif user_room == 0 and step == 5:
            print(door1_5)
        elif user_room == 1:
            print(floor_1[0])
        elif user_room == 2:
            if "snake" not in defeated_foes:
                print(floor_1[1])
            elif "snake" in defeated_foes:
                print(snake_death)
        elif user_room == 3:
            print(floor_1[2])
        elif user_room == 4:
            if "lazer gun" not in user_items:
                print(floor_1[3])
            elif "lazer gun" in user_items:
                print(lazer_gun_grab)
        elif user_room == 5:
            print(floor_1[4])
    elif user_floor == floor_2:
        if user_room == 6 and step == 1:
            print(door2_1)
        elif user_room == 6 and step == 2:
            print(door2_2)
        elif user_room == 6 and step == 3:
            print(door2_3)
        elif user_room == 6 and step == 4:
            print(door2_4)
        elif user_room == 6 and step == 5:
            print(door2_5)
        elif user_room == 7:
            if "monster" not in defeated_foes:
                print(floor_2[0])
            elif "monster" in defeated_foes:
                print(monster_death)
        elif user_room == 8:
            print(floor_2[1])
        elif user_room == 9:
            if "fireballs" not in user_items:
                print(floor_2[2])
            elif "fireballs" in user_items:
                print(fireballs_grab)
        elif user_room == 10:
            print(floor_2[3])
        elif user_room == 11:
            print(floor_2[4])
    elif user_floor == floor_3:
        if user_room == 12 and step == 1:
            print(door3_1)
        elif user_room == 12 and step == 2:
            print(door3_2)
        elif user_room == 12 and step == 3:
            print(door3_3)
        elif user_room == 12 and step == 4:
            print(door3_4)
        elif user_room == 12 and step == 5:
            print(door3_5)
        elif user_room == 13:
            print(floor_3[0])
        elif user_room == 14:
            print(floor_3[1])
        elif user_room == 15:
            if "coin monster" not in defeated_foes:
                print(floor_3[2])
            elif "coin monster" in defeated_foes:
                print(prize_final)
        elif user_room == 16:
            if "single coin" not in user_items:
                print(floor_3[3])
            elif "single coin" in user_items:
                print(single_coin_grab)
        elif user_room == 17:
            print(floor_3[4])
# Gets the user input, determines if the input is valid, and 
# returns that input if valid.  It will continue to ask until valid input is found.
def get_user_input():
    player_move = input("Choose a command: ('left', 'right', 'up', 'down', 'grab', 'open', 'fight', 'leave') ")
    if player_move in valid_moves:
        return player_move
    elif player_move not in valid_moves:
        print("A valid command was not selected. Try again. ")
        get_user_input()
    # Get a move from the user and make sure its valid
    
# Processes the user input.  Sets any game level variables
def process_move(player_move):
    # Do everything that happens as a result of the player's move
    if (player_move == 'left'):
        do_move_left()
    elif (player_move == 'right'):
        do_move_right()
    elif (player_move == 'up'):
        do_move_up()
    elif (player_move == 'down'):
        do_move_down()
    elif (player_move == 'grab'):
        do_grab()
    elif (player_move == 'open'):
        do_open()
    elif (player_move == 'fight'):
        do_fight()
    elif (player_move == 'leave'):
        do_leave()

# Relay the result of the previous move to the user.  Determine if the user won
# or lost the game and set variables accordingly
def check_game_status():
    global user_room
    global user_floor
    global step
    if user_room not in instant_death:
        return True
    elif user_room in instant_death:
        if user_room == 5:
            print(floor_1[4])
        elif user_room == 8:
            print(floor_2[1])
        elif user_room == 13:
            print(floor_3[0])
        elif user_room == 17:
            print(floor_3[4])
        print("You lost the game! GAME OVER!")
        
# Helper functions that may be useful
#Command to move left
def do_move_left():
    global step
    if user_room in hall_numbers:
        if step > 1:
            step = step - 1
            return step
        elif step <= 1:
            print("You cannot move left.")
    elif user_room not in hall_numbers:
        print("You cannot move left.")
        
#Command to move right
def do_move_right():
    global step
    if user_room in hall_numbers:
        if step < 5:
            step = step + 1
            return step 
        elif step >= 5:
            print("You cannot move right.")
    elif user_room not in hall_numbers:
        print("You cannot move right.")
        
#Command to go up the stairs
def do_move_up():
    global user_floor
    global user_room
    if user_floor == floor_1 and user_room in stair_rooms:
        user_floor = floor_2
        user_room = 6
        return user_floor
        return user_room
    elif user_floor == floor_2 and user_room in stair_rooms:
        user_floor = floor_3
        user_room = 12
        return user_floor
        return user_room
    elif user_room not in stair_rooms:
        print("There are no stairs.")
        
#Command to go down the stairs
def do_move_down():
    global user_floor
    global user_room
    if user_floor == floor_2 and user_room in stair_rooms:
        user_floor = floor_1
        user_room = 0
        return user_floor
        return user_room
    elif user_floor == floor_3 and user_room in stair_rooms:
        user_floor = floor_2
        user_room = 6
        return user_floor
        return user_room
    elif user_room not in stair_rooms:
        print("There are no stairs.")
        
#Command to grab items
def do_grab():
    if user_room == 4:
        if "lazer gun" not in user_items:
            user_items.append("lazer gun")
            print("Nice! You have a lazer gun.")
            print("Items: ",user_items)
            return user_items
        elif "lazer gun" in user_items:
            print("You already grabbed this item.")
    elif user_room == 9:
        if "fireballs" not in user_items:
            user_items.append("fireballs")
            print("Nice! You have fireballs.")
            print("Items: ",user_items)
            return user_items
        elif "fireballs" in user_items:
            print("You already grabbed this item.")
    elif user_room == 16:
        if "single coin" not in user_items:
            user_items.append("single coin")
            print("Nice! You have a single gold coin.")
            print("Items: ",user_items)
            return user_items
        elif "single coin" in user_items:
            print("You already grabbed this item.")
    elif user_room not in grab_rooms:
        print("Your attempt to grab was futile.")
        
#Command to open doors
def do_open():
    global user_room
    if user_floor == floor_1:
        print("You opened the door.")
        user_room = step
        return user_room
    elif user_floor == floor_2:
        print("You opened the door.")
        user_room = 6 + step
        return user_room
    elif user_floor == floor_3:
        print("You opened the door.")
        user_room = 12 + step
        return user_room
        
#Command to fight enemies
def do_fight():
    global user_room
    if user_room == 2 and "lazer gun" in user_items:
        if "snake" not in defeated_foes:
            fight_option = input("Use the lazer gun to vanquish the snake? (yes or no) ")
            if fight_option == "yes":
                print("The snake was blasted in the head and exploded.")
                defeated_foes.append("snake")
                return defeated_foes
            elif fight_option == "no":
                print("You ran out of the room.")
                user_room = 0
                return user_room
        elif "snake" in defeated_foes:
            print("You already won this fight.")
    elif user_room == 2 and "lazer gun" not in user_items:
        print("You do not have a weapon to fight with!")
    elif user_room == 7 and "lazer gun" in user_items:
        if "monster" not in defeated_foes:
            fight_option = input("Use the lazer gun to vanquish the monster? (yes or no) ")
            if fight_option == "yes":
                print("You blasted Ray right in the face. His brains are fried onto the wall behind him and Mountain Dew Code Red oozes out of his veins.")
                defeated_foes.append("monster")
                return defeated_foes
            elif fight_option == "no":
                print("You ran out of the room.")
                user_room = 6
                return user_room
        elif "monster" in defeated_foes:
            print("You already vanquished Ray.")
    elif user_room == 7 and "lazer gun" not in user_items:
        print("You do not have a weapon to fight with!")
    elif user_room == 15 and "lazer gun" in user_items and "fireballs" in user_items:
        if "fireball blaster" not in user_items:
            mod_gun = input("Modify the lazer gun to shoot fireballs? ")
            if mod_gun == "yes":
                user_items.append("fireball blaster")
                print("The lazer gun is now a fireball blaster. Sweet!")
                print("Items: ",user_items)
                return user_items
            elif mod_gun == "no":
                print("You did not modify the gun. You also ran out of the room because you do not have the right weapon for this fight.")
                user_room = 12
                return user_room
        elif user_room == 15 and "fireball blaster" in user_items:
            fight_option = input("Use the fireball blaster to defeat the coin beast? (yes or no) ")
            if fight_option == "yes":
                print("You blasted the coin monster in the chest. He roars in pain and falls forward, breaking into thousands of tiny coins. The gold is yours for the taking!")
                defeated_foes.append("coin monster")
                return defeated_foes
            elif fight_option == "no":
                print("You ran out of the room.")
                user_room = 12
                return user_room
    elif user_room not in fight_rooms:
        print("There is nothing to fight.")
        
#Command to leave a room
def do_leave():
    global user_room
    if user_floor == floor_1:
        user_room = 0
        return user_room
    elif user_floor == floor_2:
        user_room = 6 
        return user_room
    elif user_floor == floor_3:
        user_room = 12
        return user_room

run_game()