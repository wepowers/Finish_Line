# Course: CS 30
# Period: 1
# Date created: 2020/03/11
# Date last modified: 
# Name: William Powers
# Description: Finish Line main game file

# Characters and their traits
Character = {"John Cranos": {"XP": "100",
                              "Speed": "55%",
                              "Power-Up": "Speed Boost"},
              "Juliette Stevenson": {"XP": "50",
                                     "Speed": "75%",
                                     "Power-Up": "Double XP"},
              "Stevie Jacobson": {"XP": "20",
                                  "Speed": "95%",
                                  "Power-Up": "Protection"}
              }
# Character power ups
Powerup = {"John Cranos": {"Speed Boost": 
                                {"Description": "Inventory item that skips one turn"}},
            "Juliette Stevenson": {"Double XP": 
                                    {"Description": "Receive double XP on everything"}},
            "Stevie Jacobson": {"Protection": 
                                    {"Description": "Protected from one negative obstacle"}}
            }

# Locations
Location = {"John Cranos": {"Country Side": 
                                {"Description": "Gravel Road Racing"}},
            "Juliette Stevenson": {"New York": 
                                    {"Description": "City Streets of New York"}},
            "Stevie Jacobson": {"Manhattan": 
                                    {"Description": "City Streets of Manhattan"}}
             }

# Inventory
Inventory = {"Speed Boost": "Skip one turn",
             "5 XP Power Up": "Add 5 XP",
             "10 XP Power Up": "Add 10 XP",
             "20 XP Power Up": "Add 20 XP",
             "Flat Tire": "Add one turn and lose 5 XP",
             "Dead End": "Add one turn",
             "Gas Refill": "Add one turn and lose 10 XP",
             "Traffic Jam": "Add two turns"
             }

# Character Prints
print("John Cranos:")
XP = Character["John Cranos"]["XP"]
print(f"- XP: {XP}")
Speed = Character["John Cranos"]["Speed"]
print(f"- Speed: {Speed}")
Power_Up = Character["John Cranos"]["Power-Up"]
print(f"- Power Up: {Power_Up}")

print("\n")

print("Juliette Stevenson:")
XP = Character["Juliette Stevenson"]["XP"]
print(f"- XP: {XP}")
Speed = Character["Juliette Stevenson"]["Speed"]
print(f"- Speed: {Speed}")
Power_Up = Character["Juliette Stevenson"]["Power-Up"]
print(f"- Power Up: {Power_Up}")

print("\n")

print("Stevie Jacobson:")
XP = Character["Stevie Jacobson"]["XP"]
print(f"- XP: {XP}")
Speed = Character["Stevie Jacobson"]["Speed"]
print(f"- Speed: {Speed}")
Power_Up = Character["Stevie Jacobson"]["Power-Up"]
print(f"- Power Up: {Power_Up}")

print("\n")

# Power Up Prints
print("John Cranos Power-Up:")
PU = Powerup["John Cranos"]["Speed Boost"]["Description"]
print(f"- Speed Boost: {PU}")

print("\n")

print("Juliette Stevenson Power-Up:")
PU = Powerup["Juliette Stevenson"]["Double XP"]["Description"]
print(f"- Double XP: {PU}")

print("\n")

print("Stevie Jacobson Power-Up:")
PU = Powerup["Stevie Jacobson"]["Protection"]["Description"]
print(f"- Protection: {PU}")