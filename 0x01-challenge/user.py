#!/usr/bin/python3

"""
User class
"""

class User:
    def __init__(self):
        self.__email = None

    @property
    def email(self):
        """ Getter for the email property """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter for the email property """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
