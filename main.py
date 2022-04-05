# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms
rooms = {
        'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar'},
        'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal'},
        'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff'},
        'Bazaar' : {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids'},
        'Meat Locker' : {'South': 'Bazaar', 'East': 'Quicksand Pit', 'Item': 'Fig'},
        'Quicksand Pit': {'West': 'Meat Locker', 'Item': 'Robe'},
        'Dojo': {'West': 'Bazaar', 'Boss': 'Shadowman'},
        'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry'}
    }

# Variable to track current room
# Initialized with starting room
current_room = "Liminal Space"

# List to track inventory
inventory = []

# Gameplay loop
while True:
    # Start-of-turn message
    print(f"\nYou are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")

    # Tracks current room's item if there is one
    if "Item" in rooms[current_room].keys():
        nearby_item = rooms[current_room]["Item"]

    # If there is an item in current_room that isn't in your inventory, tell the user
    if "Item" in rooms[current_room].keys():
        if nearby_item not in inventory:
            print(f"You see a {nearby_item}")

    # Accepts user input
    user_input = input('Enter your move:\n')
    # Splits move into words
    next_move = user_input.split(' ')
    # action determines what the user wants to do
    # object determines where the action is directed
    action = next_move[0]
    if len(next_move) > 1:
        object = next_move[1].title()

    # If action is 'go'
    #   set current_room to room associated with object
    if action == 'go':
        try:
            current_room = rooms[current_room][object]
        except:
            print("You can't go that way.")
    # If action is 'get'
    #   if item is present
    #       if item is not in inventory
    #           add item to inventory
    elif action == 'get':
        try:
            if object in rooms[current_room].values():
                if object not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    print(f"{object} retrieved!")
                else:
                    print(f"You already have the {object}.")
            else:
                print(f"Can't find {object}.")
        except:
            print("You can't get that item")
    # Exit command breaks while-loop and terminates program
    elif action == 'exit':
        break
    # If user_input is invalid, the user is notified and the while-loop continues
    else:
        print("Invalid command")