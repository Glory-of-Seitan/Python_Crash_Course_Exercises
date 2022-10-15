from user_module import User

class Admin(User):
    """Define an admin user with special privileges"""

    def __init__(
        self,
        username,
        first_name="admin",
        last_name="admin",
        password="admin",
        yrs_since_join=0,
        age="eternal",
    ):
        """Initialize an admin user with special privileges"""
        super().__init__(
            username,
            first_name,
            last_name,
            password,
            yrs_since_join,
            age,
        )
        self.privileges = Privileges()


class Privileges:
    """A class that defines user privileges"""

    def __init__(
        self,
        privileges=[
            "can add post",
            "can delete post",
            "can ban user",
        ],
    ):
        """Initialize user privileges"""
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nThis user has the following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")
