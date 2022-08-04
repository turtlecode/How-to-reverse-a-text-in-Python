
# Python3 code to reverse the lines
# of a file using Stack.
   
      
# Creating Stack class (LIFO rule)
class Stack:
      
    def __init__(self):
          
        # Creating an empty stack
        self._arr = []
          
    # Creating push() method.
    def push(self, val):
        self._arr.append(val)
   
    def is_empty(self):
          
        # Returns True if empty
        return len(self._arr) == 0
  
    # Creating Pop method.
    def pop(self):
          
        if self.is_empty():
            print("Stack is empty")
            return
          
        return self._arr.pop()
  
# Creating a function which will reverse
# the lines of a file and Overwrites the 
# given file with its contents line-by-line
# reversed
def reverse_file(filename):
       
    S = Stack()
    original = open(filename)
      
    for line in original:
        S.push(line.rstrip("\n"))
      
    original.close()
       
       
    output = open(filename, 'w')
      
    while not S.is_empty():
        output.write(S.pop()+"\n")
      
    output.close()
  
  
# Driver Code
filename = "GFG.txt"
  
# Calling the reverse_file function
reverse_file(filename)
   
# Now reading the content of the file
with open(filename) as file:
        for f in file.readlines():
            print(f, end ="")