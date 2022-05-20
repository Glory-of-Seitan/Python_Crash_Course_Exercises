def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_albert = build_profile(
    "albert",
    "einstein",
    location="princeton",
    field="physics",
)

user_me = build_profile(
    "john",
    "corrigan",
    hobby="D&D",
    age="in my 30s",
    eyes="brown",
)

print(user_me)
