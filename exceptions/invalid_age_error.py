"""Define a custom exception"""

class InvalidAgeError(Exception):
    """Exception raised for invalid age inputs"""
    def __init__(self, age, message="Age must be between 18 and 65"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    