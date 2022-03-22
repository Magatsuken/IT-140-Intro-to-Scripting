# Nicholas Truong
rooms = {
    'Entrance': {'east': 'Living Room'},
    'Living Room': {'north': 'Bedroom', 'east': 'Study', 'west': 'Entrance', 'south': 'Kitchen'},
    'Bedroom': {'east': 'Closet', 'south': 'Living Room'},
    'Closet': {'west': 'Bedroom'},
    'Study': {'west': 'Living Room', 'north': 'Hidden Room'},
    'Hidden Room': {'south': 'Study'},
    'Kitchen': {'north': 'Living Room', 'east': 'Bathroom'},
    'Bathroom': {'west': 'Kitchen'}
}
# Rooms of the game
items = {
    'Living Room': {'keys'},
    'Bedroom': {'body'},
    'Hidden Room': {'footprints'},
    'Study': {'fingerprints'},
    'Kitchen': {'murder weapon'},
    'Bathroom': {'notes'}
}
# Items in a room
inventory = []
# Initializes inventory
currentRoom = 'Entrance'
# Entrance is default room
gameStatus = 'Playing'
# gameStatus determines if the game is still playing or if it is over
def player_intro():
    print('\nYour goal is to gather evidence in each room and put the ghost to rest.')
    print('You will lose if you find the ghost without sufficient evidence.\n')
    print("Type 'move' to move from room to room.")
    print("Type 'status' to see what room you are in and what items are in this room.")
    print("Type 'item' to grab the items in this room.")
    print("Type 'quit' to quit the game.\n")
    # Shows user controls and goal of the game
def player_move(room):
    # If user types 'move' move to different rooms
    while True:
        if room == 'Closet':
            print('\nBe careful! The Ghost haunts this room!')
            # Shows the user that the closet is dangerous
        print('\nYou are currently in: ' + room)
        # Outputs player's current room
        print('You can move ' + str(rooms[room]))
        # Shows what direction the user can move and what room you can move to
        print("Type 'stop' to stop in the current room.")
        # If the user types 'stop', they stop in the current room
        direction = input('Where do you want to go?\n').lower()
        # Takes user input and changes it to lower case
        if direction in rooms[room]:
            room = rooms[room][direction]
            # If the user input is a valid direction, then change current room into new room based on dict
        elif direction == 'stop':
            print('\nStopped in ' + room + '\n')
            return room
            # If user input is 'stop', stop in the current room
        else:
            print('Invalid move.')
            # If the user input is invalid, return invalid move
def player_status():
    print('\nYou are currently in: ' + currentRoom)
    # Shows the user what room they are in currently
    if inventory != []:
        print('Your evidence: ' + str(inventory))
    # Shows the user the items in their inventory
    else:
        print('Your evidence: None')
    if currentRoom in items:
        print('Here are the items in this room: ' + str(items[currentRoom]) + '\n')
        # Shows the user the items in a room
    else:
        print('No items in ' + currentRoom + '\n')
        # If there are no items in the room, show the user that there is nothing in the room
def player_grabitem():
    if currentRoom in items:
        inventory.append(items[currentRoom])
        print('\n' + str(items[currentRoom]) + ' added to evidence.\n')
        items.pop(currentRoom)
        # If the user types in 'item', the item is added to their inventory and removed from the room
    else:
        print('Nothing of value here.')
        # Tells the user there are no items to grab
def player_lose():
    print("The Ghost is here! You don't have enough evidence to solve their murder...")
    gameStatus = 'Game Over'
    # Lose condition. If user doesn't have enough evidence and stops in the closet, they lose
def player_winning():
    print("You have enough evidence to put the Ghost to rest! They are in the Closet!\n")
    # Prompts the user that they have enough items to win the game
def player_victory():
    print("You solved the mystery murder and put the Ghost to rest!")
    gameStatus = 'Game Over'
    # Win condition. If user has enough evidence and they are in the closet, they win
while gameStatus != 'Game Over':
    print("Type 'info' for more information.")
    action = input('What do you want to do?\n').lower()
    # Ask for user input
    if action == 'info':
        player_intro()
    if action == 'move':
        currentRoom = player_move(currentRoom)
    if action == 'quit':
        gameStatus = 'Game Over'
        # If user types 'quit', the game ends
    if action == 'status':
        player_status()
    if action == 'item':
        player_grabitem()
    if currentRoom == 'Closet' and len(inventory) != 6:
        player_lose()
    if len(inventory) == 6 and currentRoom != 'Closet':
        player_winning()
    if currentRoom == 'Closet' and len(inventory) == 6:
        player_victory()
input('\nThanks for playing! Press any key to continue.')