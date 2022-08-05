# Python3 code to reverse the lines of a file


# Creating a function which will reverse
# the lines of a file and overwrites the 
# given file with its contents reversed

def reverse_file(filename):
    with open(filename, "r") as file:
        raw = file.read()
 
    rawLines = raw.split("\n")
    reversedLines = reversed(rawLines)
    parsed = "\n".join(reversedLines)
 
    with open(filename, "w") as file:
        file.write(parsed)


# Driver Code
filename = "GFG.txt"

# Calling the reverse_file function
reverse_file(filename)

# Now reading the contents of the file
with open(filename, "r") as file:
    print(file.read())
