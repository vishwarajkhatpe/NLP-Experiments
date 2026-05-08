# Experiment 5
# Morphology using Add-Delete Table

# Input words
root_word = "play"
modified_word = "playing"

# Find common root
common = ""

for i in range(min(len(root_word), len(modified_word))):

    if root_word[i] == modified_word[i]:
        common += root_word[i]

    else:
        break

# Find deleted part
delete_part = root_word[len(common):]

if delete_part == "":
    delete_part = "NULL"

# Find added part
add_part = modified_word[len(common):]

if add_part == "":
    add_part = "NULL"

# Display output
print("Root Word :", root_word)
print("Modified Word :", modified_word)

print("\nAdd-Delete Table")

print("Delete :", delete_part)
print("Add    :", add_part)