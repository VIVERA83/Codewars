"""Person Class Bug 7kyu"""
# The following code was thought to be working properly, however when the code tries to access the age of the
# person instance it fails.

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f"{self.first_name} {self.last_name}"