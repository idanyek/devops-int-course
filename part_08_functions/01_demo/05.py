def show_employee(name: str, salary: int = 9000):
    return f"{name} salary: {salary}"


print(show_employee("ben", 12000))
print(show_employee("Jessa"))
