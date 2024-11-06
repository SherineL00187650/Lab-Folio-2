# Simple Maze Game

# Define the maze layout with rooms and connections
maze = {
    'Start': {'north': 'A', 'east': 'B', 'item': None},
    'A': {'south': 'Start', 'north': 'C', 'east': 'D', 'item': 'key'},
    'B': {'west': 'Start', 'north': 'D', 'east': 'Exit', 'item': 'map'},
    'C': {'south': 'A', 'item': None},
    'D': {'west': 'A', 'south': 'B', 'north': 'Exit', 'item': None},
    'Exit': {'south': 'D', 'west': 'B', 'item': 'treasure'}
}

# Initialize player state
inventory = []
current_room = 'Start'

def show_instructions():
    print("""
Welcome to the Maze Game!
Find the exit and collect items along the way.
Commands:
  - go [direction] (north, south, east, west)
  - get [item]
  - quit
Objective: Find the 'treasure' at the exit. Good luck!
""")

def show_status():
    print("\n---------------------------")
    print(f"You are in room {current_room}.")
    print("Inventory:", inventory)
    if 'item' in maze[current_room] and maze[current_room]['item']:
        print(f"You see a {maze[current_room]['item']} here.")
    print("---------------------------")

def move(direction):
    global current_room
    if direction in maze[current_room]:
        next_room = maze[current_room][direction]
        if next_room == 'Exit' and 'key' not in inventory:
            print("The door to the exit is locked! You need a key.")
        else:
            current_room = next_room
    else:
        print("You can't go that way.")

def get_item(item):
    if 'item' in maze[current_room] and maze[current_room]['item'] == item:
        print(f"You picked up the {item}.")
        inventory.append(item)
        maze[current_room]['item'] = None
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
        if current_room == 'Exit' and 'treasure' in inventory:
            print("Congratulations! You found the treasure and exited the maze!")
            break

# Run the game
if __name__ == "__main__":
    main()
