# Demonstrates how to use tuples

# Create a tuple
inventory = ()

if not inventory:
	print("You are empty handed")

input("\nPress the enter key to continue.")

# Add stuff to inventory
inventory = (
	"apples",
	"blueberries",
	"helmet",
	"potion")

print("\nThe tuple inventory is: \n", inventory)

# Print each separately
print("\nYour items are:")
for item in inventory:
    print(item)

# check the length
print("You have ", len(inventory), " items")

# If statements to check contents
if "potion" in inventory:
	print("You brought your potion right?\n")
else:
	print("Suck it!")

if "drugs" in inventory:
	print("Drugs!")
else:
	print("\nno drugs")

print("\nPress enter to quit.")
