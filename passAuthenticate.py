import urllib.request
import re

with urllib.request.urlopen('http://pointzi.com') as response:
    html = response.read()
    print(html)

class Authentication(str):

    def _init_(self):
        self = ''

    def __lower(self):
        lower = any(ch.islower() for ch in self)
        return lower

    def __upper(self):
        upper = any(ch.isupper() for ch in self)
        return upper

    def __digit(self):
        digit = any(ch.isdigit() for ch in  self)
        return digit

    def __special(self):
        special = (bool(re.search('^[a-zA-Z0-9]*$',self))!=True)
        return special

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()
        special = self.__special()

        length = len(self)

        report =  lower and special and upper and digit and length >= 6

        if report:
            print("Password passed all checks ")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False

        elif not upper:
            print("You didnt use Upper case letter")
            return False

        elif length <6:
            print("Password should Atleast have 6 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False

        elif not special:
            print("You didnt use special case")
            return False

        else:
            pass

C = Authentication("hellMotto2@")
print(C.validate())