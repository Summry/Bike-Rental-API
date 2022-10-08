class Person():
    def __init__(self, name, age):

        if (type(name) == str and len(name) >= 3):
            self.name = name
        else:
            raise AttributeError("Name must be a string with 3+ characters!")
        
        if (type(age) == int and age > 0):
            self.age = age
        else:
            raise AttributeError("Age must be positive number!")

    def get_name(self):
        return f"{self.name.upper()} / {self.age}"
