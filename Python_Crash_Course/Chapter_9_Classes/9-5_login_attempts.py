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
        self.log_attmps = 0

    def desc_user(self):
        """Describes one user's info"""
        print(f"\nUser's real name = {self.f_name} {self.l_name}")
        print(f"User's password = {self.pw}")
        print(f"Years on the site = {self.yrs}")
        print(f"User age = {self.age}")

    def greet_user(self):
        """Greets a user upon login to the site"""
        print(f"Welcome {self.f_name}. You are now logged in.")

    def increment_log_attmps(self, times):
        for time in range(0, times):
            self.log_attmps += 1

    def reset_log_attmps(self):
        self.log_attmps = 0


user_1 = User("John", "Crabapple", 123456, 5, 31)
user_1.desc_user()
user_1.greet_user()
print(user_1.log_attmps)

user_1.increment_log_attmps(5)
print(user_1.log_attmps)

user_1.increment_log_attmps(1)
print(user_1.log_attmps)

user_1.reset_log_attmps()
print(user_1.log_attmps)
