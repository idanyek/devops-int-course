user = {
    "id": 4170,
    "password": "Password123$!",
    "first_name": "idan",
    "last_name": "yekutiel"
}

user["secret"] = user.pop("password")
user["surename"] = user.pop("last_name")

print(user)