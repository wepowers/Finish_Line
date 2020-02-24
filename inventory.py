# Course: CS 30
# Period: 1
# Date created: 2020/02/13
# Date last modified: 2020/02/24
# Name: William Powers
# Description: Text Based Game

# Obstacles that you can run into that will help you to win
positive_obstacle = ['Speed Boost', '5 XP Power Up', '10 XP Power Up',
                     '20 XP Power Up']
print(positive_obstacle)
message = f"You have found a {positive_obstacle[0]}."
print(message)
message = f"You have found a {positive_obstacle[1]}."
print(message)
message = f"You have found a {positive_obstacle[2]}."
print(message)
message = f"You have found a {positive_obstacle[3]}."
print(message)
print(sorted(positive_obstacle))

print("\n")

# Obstacles that you can run into that will make it harder to win
negative_obstacle = ['Flat Tire', 'Dead End', 'Gas Refill', 'Traffic Jam']
print(negative_obstacle)
message = f"Oh no! {negative_obstacle[0]}."
print(message)
message = f"Oh no! {negative_obstacle[1]}."
print(message)
message = f"Oh no! {negative_obstacle[2]}."
print(message)
message = f"Oh no! {negative_obstacle[3]}."
print(message)
print(negative_obstacle)
negative_obstacle.sort()
print(negative_obstacle)

print("\n")

# List of what you have in your inventory
inventory = ['50 XP', 'Speed Boost', 'Free Life']
message = f"Your inventory includes: {inventory}."
print(message)
print(inventory)
inventory.append('Speed Boost')
print(inventory)
inventory.insert(0, 'Speed Boost')
print(inventory)
del inventory[0]
print(inventory)
popped_inventory = inventory.pop()
print(inventory)
print(popped_inventory)
inventory.remove('Free Life')
print(inventory)
inventory.reverse()
print(inventory)
print(len(inventory))