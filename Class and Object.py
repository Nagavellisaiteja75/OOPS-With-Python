class Developer:
    # The __init__ method initializes the object's attributes (state)
    def __init__(self, name, language):
        self.name = name
        self.language = language

    # A method defining an action the object can take (behavior)
    def write_code(self):
        print(f"{self.name} is writing code in {self.language}.")

# Creating an object (instantiation)
dev1 = Developer("Alice", "Python")

# Calling the object's method
dev1.write_code() 
# Output: Alice is writing code in Python.