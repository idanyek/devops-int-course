password = input("enter password: ")
password_confirm = input("enter password confirmation: ")

if len(password) < 7:
    print("short")
elif password != password_confirm:
    print("Diffrenece")
else:
    print("OK")