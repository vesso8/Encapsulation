class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if 5 < len(value) < 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if self.length_long(value) and self.upper_case_letter(value) and self.is_digit(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
    def length_long(self, password):
        return len(password) >= 8
    def upper_case_letter(self, password):
        upper_case = [letters for letters in password if letters.isupper()]
        if upper_case:
            return True
        else:
            return False
    def is_digit(self, password):
        digits_case = [digits for digits in password if digits.isdigit()]
        if digits_case:
            return True
        else:
            return False
    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)