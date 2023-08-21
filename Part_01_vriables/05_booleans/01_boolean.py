status = True
my_status = False

print(f"{status} is {type(status)}")
print(f"{my_status} is {type(my_status)}")

print(int(status)) # 1
print(int(my_status)) # 0

print(float(status)) #1.0
print(float(my_status)) #0.0

print(f"bool(1) -> {bool(1)}") # True
print(f"bool(0) -> {bool(0)}") # False
print(f"bool(-1) -> {bool(-1)}") # True
print(f"bool(200) -> {bool(200)}") # True

print(f"bool(none) -> {bool(None)}") # False

print(f"bool('kuti') -> {bool('kuti')}") # True
print(f"bool(' ') -> {bool(' ')}") # True
print(f"bool('') -> {bool('')}") # False
