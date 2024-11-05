import sys

# Define the rooms and their connections
rooms = {
    'Entrance': {'north': 'Hall', 'item': None},
    'Hall': {'south': 'Entrance', 'east': 'Kitchen', 'west': 'Library', 'item': 'map'},
    'Library': {'east': 'Hall', 'north': 'Garden', 'item': 'book'},
    'Kitchen': {'west': 'Hall', 'north': 'Dining Room', 'item': 'key'},
    'Dining Room': {'south': 'Kitchen', 'item': 'monster'},
    'Garden': {'south': 'Library', 'item': 'flower'}
}

# Initialize game variables
inventory = []
current_room = 'Entrance'

def show_instructions():
    print("""
Welcome to the Adventure Game!
Navigate through rooms, collect items, and avoid monsters to win.
Commands:
  - go [direction] (north, south, east, west)
  - get [item]
  - quit
Collect the 'flower' to win. Beware of the 'monster'!
""")

def show_status():
    print("\n---------------------------")
    print(f"You are in the {current_room}.")
    print("Inventory:", inventory)
    if 'item' in rooms[current_room] and rooms[current_room]['item']:
        print(f"You see a {rooms[current_room]['item']} here.")
    print("---------------------------")

def move(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        if current_room == 'Dining Room' and 'key' not in inventory:
            print("A monster caught you in the Dining Room! You need a key to escape. Game over.")
            sys.exit()
    else:
        print("You can't go that way.")

def get_item(item):
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
        print(f"You picked up the {item}.")
        inventory.append(item)
        rooms[current_room]['item'] = None
    else:
        print(f"There is no {item} here to take.")

def main():
    show_instructions()
    
    while True:
        show_status()
        
        # Get user input
        command = input("Enter your command: ").split()
        
        if command[0] == 'go':
            if len(command) > 1:
                move(command[1])
            else:
                print("Go where? Specify a direction (north, south, east, west).")
        
        elif command[0] == 'get':
            if len(command) > 1:
                get_item(command[1])
            else:
                print("Get what? Specify an item.")
        
        elif command[0] == 'quit':
            print("Thanks for playing!")
            break

        else:
            print("Invalid command. Try 'go [direction]', 'get [item]', or 'quit'.")
        
        # Check for win condition
        if 'flower' in inventory:
            print("Congratulations! You found the flower and won the game!")
            break

# Run the game
if __name__ == "__main__":
    main()
