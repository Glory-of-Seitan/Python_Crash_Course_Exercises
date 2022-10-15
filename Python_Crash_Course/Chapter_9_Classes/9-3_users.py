class User:
    """Describe simulated users of a website"""

    def __init__(
        self,
        first_name,
        last_name,
        password,
        yrs_since_join,
        age,
    ):
        self.f_name = first_name
        self.l_name = last_name
        self.pw = password
        self.yrs = yrs_since_join
        self.age = age

    def desc_user(self):
        """Describes one user's info"""
        print(f"\nUser's real name = {self.f_name} {self.l_name}")
        print(f"User's password = {self.pw}")
        print(f"Years on the site = {self.yrs}")
        print(f"User age = {self.age}")

    def greet_user(self):
        """Greets a user upon login to the site"""
        print(f"Welcome {self.f_name}. You are now logged in.")


user_1 = User("John", "Crabapple", 123456, 5, 31)
user_1.desc_user()
user_1.greet_user()

user_2 = User("Dingo", "Simons", "password", 2, 57)
user_2.desc_user()
user_2.greet_user()

user_3 = User("Kelly", "Roomba", "1kjdsh902834oihdsf", 3, 26)
user_3.desc_user()
user_3.greet_user()
